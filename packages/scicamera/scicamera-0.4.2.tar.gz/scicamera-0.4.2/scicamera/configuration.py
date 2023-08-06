from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from logging import getLogger
from typing import TYPE_CHECKING, Any, Dict, Optional, Tuple

import libcamera

from scicamera import formats
from scicamera.controls import Controls
from scicamera.lc_helpers import errno_handle

if TYPE_CHECKING:
    from scicamera.camera import Camera

_log = getLogger(__name__)


def _assert_type(thing: Any, type_) -> None:
    if not isinstance(thing, type_):
        raise TypeError(f"{thing} should be a {type_} not {type(thing)}")


_raw_stream_ignore_list = [
    "bit_depth",
    "crop_limits",
    "exposure_limits",
    "fps",
    "unpacked",
]

STILL = libcamera.StreamRole.StillCapture
RAW = libcamera.StreamRole.Raw
VIDEO = libcamera.StreamRole.VideoRecording
VIEWFINDER = libcamera.StreamRole.Viewfinder


@dataclass
class StreamConfig:
    size: tuple[int, int]
    format: Optional[str] = None
    stride: Optional[int] = None
    framesize: Optional[int] = None

    @classmethod
    def from_lc_stream_config(cls, libcamera_stream_config):
        return cls(
            format=str(libcamera_stream_config.pixel_format),
            size=(
                libcamera_stream_config.size.width,
                libcamera_stream_config.size.height,
            ),
            stride=libcamera_stream_config.stride,
            framesize=libcamera_stream_config.frame_size,
        )

    def make_dict(self):
        return asdict(self)

    def align(self, optimal=True):
        if optimal:
            # Adjust the image size so that all planes are a mutliple of 32 bytes wide.
            # This matches the hardware behaviour and means we can be more efficient.
            align = 32
            if self.format in ("YUV420", "YVU420"):
                align = 64  # because the UV planes will have half this alignment
            elif self.format in ("XBGR8888", "XRGB8888"):
                align = (
                    16  # 4 channels per pixel gives us an automatic extra factor of 2
                )
        else:
            align = 2
        self.size = (
            self.size[0] - self.size[0] % align,
            self.size[1] - self.size[1] % 2,
        )

    def __post_init__(self) -> None:
        self.check("internal")

    def check(self, name: str):
        """Check the configuration of the passed in config.

        Raises RuntimeError if the configuration is invalid.
        """
        # Check the parameters for a single stream.
        if self.format not in [None, "MJPEG"]:
            _assert_type(self.format, str)

            if name == "raw":
                if not formats.is_raw(self.format):
                    raise RuntimeError("Unrecognized raw format " + self.format)
            else:
                if not formats.is_format_valid(self.format):
                    raise RuntimeError(
                        "Bad format " + self.format + " in stream " + name
                    )

        _assert_type(self.size, tuple)
        if len(self.size) != 2:
            raise RuntimeError(
                f"size in {name} stream should be (width, height) got: {self.size}"
            )

        for i in range(2):
            if self.size[i] % 2:
                raise RuntimeError(
                    f"All dimensions in {name} stream should be even got: {self.size}"
                )


@dataclass
class CameraConfig:
    camera: Camera
    use_case: str
    buffer_count: int
    transform: libcamera._libcamera.Transform
    color_space: libcamera._libcamera.ColorSpace

    # The are allowed to be a dict when user input, but will
    # be transformed to the proper class by the __post_init__ method.
    controls: Controls | dict
    main: StreamConfig | dict
    lores: Optional[StreamConfig | dict] = None
    raw: Optional[StreamConfig | dict] = None

    # This is set only after validation by libcamera
    libcamera_config: Optional[Any] = None

    def get_stream_config(self, name: str) -> StreamConfig | None:
        return {
            "main": self.main,
            "lores": self.lores,
            "raw": self.raw,
        }[name]

    def enable_lores(self, enable: bool = True) -> None:
        self.lores = (
            StreamConfig(size=self.main.size, format="YUV420") if enable else None
        )

    def enable_raw(self, enable: bool = True) -> None:
        self.raw = (
            StreamConfig(size=self.main.size, format=self.camera.sensor_format)
            if enable
            else None
        )

    def align(self, optimal: bool = True):
        self.main.align(optimal)
        if self.lores is not None:
            self.lores.align(optimal)
        # No sense trying to align the raw stream.

    def get_stream_indices(self) -> Tuple[int, int, int]:
        """Get the main, lores, and raw stream indices.

        These indices will be -1 if unset.
        """
        # Get the indices of the streams we want to use.
        index = 1
        lores_index = -1
        raw_index = -1
        if self.lores is not None:
            lores_index = index
            index += 1
        if self.raw is not None:
            raw_index = index
        return 0, lores_index, raw_index

    def __post_init__(self) -> None:
        if isinstance(self.controls, dict):
            _log.warning("CameraConfiguration controls should be a Controls object")
            self.controls = Controls(self.camera, self.controls)
        if isinstance(self.main, dict):
            _log.warning("CameraConfiguration 'main' should be a StreamConfiguration")
            self.main = StreamConfig(**self.main)
        if isinstance(self.lores, dict):
            _log.warning("CameraConfiguration 'lores' should be a StreamConfiguration")
            self.lores = StreamConfig(**self.lores)
        if isinstance(self.raw, dict):
            _log.warning("CameraConfiguration 'raw' should be a StreamConfiguration")
            self.raw = StreamConfig(**self.raw)

        # Check the entire camera configuration for errors.
        _assert_type(self.color_space, libcamera._libcamera.ColorSpace)
        _assert_type(self.transform, libcamera._libcamera.Transform)

        self.main.check("main")
        if self.lores is not None:
            self.lores.check("lores")
            main_w, main_h = self.main.size
            lores_w, lores_h = self.lores.size
            if lores_w > main_w or lores_h > main_h:
                raise RuntimeError("lores stream dimensions may not exceed main stream")
            if not formats.is_YUV(self.lores.format):
                raise RuntimeError("lores stream must be YUV")

        if self.raw is not None:
            self.raw.check("raw")

    # TODO(meawoppl) - These can likely be made static/hoisted
    @classmethod
    def for_preview(
        cls,
        camera: Camera,
        main: dict = {},
        lores=None,
        raw=None,
        transform=libcamera.Transform(),
        color_space=libcamera.ColorSpace.Sycc(),
        buffer_count=4,
        controls={},
    ) -> CameraConfig:
        """Make a configuration suitable for camera preview."""
        main_stream = StreamConfig(format="XBGR8888", size=(640, 480))
        main_stream = replace(main_stream, **main)
        main_stream.align(optimal=False)

        if lores is not None:
            lores_stream = StreamConfig(format="YUV420", size=main_stream.size)
            lores_stream = replace(lores_stream, **lores)
            lores_stream.align(optimal=False)
        else:
            lores_stream = None

        if raw is not None:
            raw_stream = StreamConfig(
                format=camera.sensor_format, size=camera.sensor_resolution
            )
            updates: dict = raw.copy()
            for name in _raw_stream_ignore_list:
                updates.pop(name, None)
            raw_stream = replace(raw_stream, **updates)
        else:
            raw_stream = None
        # Let the framerate vary from 12fps to as fast as possible.
        if (
            "NoiseReductionMode" in camera.camera_controls
            and "FrameDurationLimits" in camera.camera_controls
        ):
            controls = {
                "NoiseReductionMode": libcamera.controls.draft.NoiseReductionModeEnum.Minimal,
                "FrameDurationLimits": (100, 83333),
            } | controls
        return cls(
            camera=camera,
            use_case="preview",
            transform=transform,
            color_space=color_space,
            buffer_count=buffer_count,
            controls=controls,
            main=main_stream,
            lores=lores_stream,
            raw=raw_stream,
        )

    @classmethod
    def for_still(
        cls,
        camera,
        main={},
        lores=None,
        raw=None,
        transform=libcamera.Transform(),
        color_space=libcamera.ColorSpace.Sycc(),
        buffer_count=1,
        controls={},
    ) -> CameraConfig:
        """Make a configuration suitable for still image capture. Default to 2 buffers, as the Gl preview would need them."""
        main_stream = StreamConfig(format="BGR888", size=camera.sensor_resolution)
        main_stream = replace(main_stream, **main)
        main_stream.align(optimal=False)

        if lores is not None:
            lores_stream = StreamConfig(format="YUV420", size=main_stream.size)
            lores_stream = replace(lores_stream, **lores)
            lores_stream.align(optimal=False)
        else:
            lores_stream = None

        if raw is not None:
            raw_stream = StreamConfig(
                format=camera.sensor_format, size=main_stream.size
            )
            raw_stream = replace(raw_stream, **raw)
        else:
            raw_stream = None
        # Let the framerate span the entire possible range of the sensor.
        if (
            "NoiseReductionMode" in camera.camera_controls
            and "FrameDurationLimits" in camera.camera_controls
        ):
            controls = {
                "NoiseReductionMode": libcamera.controls.draft.NoiseReductionModeEnum.HighQuality,
                "FrameDurationLimits": (100, 1000000 * 1000),
            } | controls
        return cls(
            camera=camera,
            use_case="still",
            transform=transform,
            color_space=color_space,
            buffer_count=buffer_count,
            controls=controls,
            main=main_stream,
            lores=lores_stream,
            raw=raw_stream,
        )

    @classmethod
    def for_video(
        cls,
        camera: Camera,
        main={},
        lores=None,
        raw=None,
        transform=libcamera.Transform(),
        color_space=None,
        buffer_count=6,
        controls={},
    ) -> CameraConfig:
        """Make a configuration suitable for video recording."""
        main_stream = StreamConfig(format="XBGR8888", size=(1280, 720))
        main_stream = replace(main_stream, **main)
        main_stream.align(optimal=False)

        if lores is not None:
            lores_stream = StreamConfig(format="YUV420", size=main_stream.size)
            lores_stream = replace(lores_stream, **lores)
            lores_stream.align(optimal=False)
        else:
            lores_stream = None

        if raw is not None:
            raw_stream = StreamConfig(
                format=camera.sensor_format, size=main_stream.size
            )
            raw_stream = replace(raw_stream, **raw)
        else:
            raw_stream = None

        if color_space is None:
            # Choose default color space according to the video resolution.
            if formats.is_RGB(main_stream.format):
                # There's a bug down in some driver where it won't accept anything other than
                # sRGB or JPEG as the color space for an RGB stream. So until that is fixed:
                color_space = libcamera.ColorSpace.Sycc()
            elif main_stream.size[0] < 1280 or main_stream.size[1] < 720:
                color_space = libcamera.ColorSpace.Smpte170m()
            else:
                color_space = libcamera.ColorSpace.Rec709()
        if (
            "NoiseReductionMode" in camera.camera_controls
            and "FrameDurationLimits" in camera.camera_controls
        ):
            controls = {
                "NoiseReductionMode": libcamera.controls.draft.NoiseReductionModeEnum.Fast,
                "FrameDurationLimits": (33333, 33333),
            } | controls
        return cls(
            camera=camera,
            use_case="video",
            transform=transform,
            color_space=color_space,
            buffer_count=buffer_count,
            controls=controls,
            main=main_stream,
            lores=lores_stream,
            raw=raw_stream,
        )

    def _update_libcamera_stream_config(
        self, libcamera_stream_config, stream_config: StreamConfig, buffer_count: int
    ) -> None:
        # Update the libcamera stream config with ours.
        libcamera_stream_config.size = libcamera.Size(*stream_config.size)
        libcamera_stream_config.pixel_format = libcamera.PixelFormat(
            stream_config.format
        )
        libcamera_stream_config.buffer_count = buffer_count

    def apply(self, lc_camera) -> Dict[str, Any]:
        # Make a libcamera configuration object from our Python configuration.

        # We will create each stream with the "viewfinder" role just to get the stream
        # configuration objects, and note the positions our named streams will have in
        # libcamera's stream list.
        roles = [VIEWFINDER]
        main_index, lores_index, raw_index = self.get_stream_indices()
        if self.lores is not None:
            roles += [VIEWFINDER]
        if self.raw is not None:
            roles += [RAW]

        # Make the libcamera configuration, and then we'll write all our parameters over
        # the ones it gave us.
        libcamera_config = lc_camera.generate_configuration(roles)
        if libcamera_config is None:
            raise RuntimeError(
                f"Failed to generate libcamera configuration for {self} using {lc_camera}"
            )
        libcamera_config.transform = self.transform
        self._update_libcamera_stream_config(
            libcamera_config.at(main_index), self.main, self.buffer_count
        )
        libcamera_config.at(main_index).color_space = self.color_space
        if self.lores is not None:
            self._update_libcamera_stream_config(
                libcamera_config.at(lores_index),
                self.lores,
                self.buffer_count,
            )
            libcamera_config.at(lores_index).color_space = self.color_space

        if self.raw is not None:
            self._update_libcamera_stream_config(
                libcamera_config.at(raw_index), self.raw, self.buffer_count
            )
            libcamera_config.at(raw_index).color_space = libcamera.ColorSpace.Raw()

        # Check that libcamera is happy with it.
        _log.debug(f"Validating configuration: {self}")
        status = libcamera_config.validate()
        if status == libcamera.CameraConfiguration.Status.Invalid:
            raise RuntimeError(f"Invalid camera configuration: {self}")
        elif status == libcamera.CameraConfiguration.Status.Adjusted:
            _log.info("Camera configuration has been adjusted!")

        # Back prop any tweaks it made onto this class
        self.transform = libcamera_config.transform
        self.color_space = libcamera_config.at(0).color_space
        self.main = StreamConfig.from_lc_stream_config(libcamera_config.at(0))
        if lores_index >= 0:
            self.lores = StreamConfig.from_lc_stream_config(
                libcamera_config.at(lores_index)
            )
        if raw_index >= 0:
            self.raw = StreamConfig.from_lc_stream_config(
                libcamera_config.at(raw_index)
            )

        # Configure the lc_camera instance
        code = lc_camera.configure(libcamera_config)
        errno_handle(code, "camera.configure()")
        _log.info("Configuration successful!")
        _log.debug(f"Final configuration: {self}")

        self.libcamera_config = libcamera_config

    def get_stream_map(self) -> Dict[str, Any]:
        # Record which libcamera stream goes with which of our names.
        stream_map = {}
        for idx, name in zip(self.get_stream_indices(), ("main", "lores", "raw")):
            if idx >= 0:
                stream_map[name] = self.libcamera_config.at(idx).stream
        return stream_map
