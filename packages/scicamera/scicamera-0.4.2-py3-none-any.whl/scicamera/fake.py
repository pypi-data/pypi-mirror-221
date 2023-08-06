"""
This submodule contains a fake camera implementation that can be used for
testing purposes. All instances of the FakeCamera class will share the
same class structure so type-checking will work as expected. Similarly,
the FakeCamera class will be a subclass of RequestMachinery so it can be
used as a drop-in replacement for a real camera in basically every way.
"""
import time
from concurrent.futures import Future
from threading import Event, Thread
from typing import Any, Dict, Tuple

import libcamera
import numpy as np

from scicamera.actions import RequestMachinery
from scicamera.configuration import CameraConfig, StreamConfig
from scicamera.controls import Controls
from scicamera.info import CameraInfo
from scicamera.request import CompletedRequest
from scicamera.typing import TypedFuture

FAKE_SIZE = (320, 240)
FAKE_FORMAT = "RGB888"
FAKE_CHANNELS = 3
FAKE_STRIDE = FAKE_CHANNELS * FAKE_SIZE[0]


def make_fake_image(shape: Tuple[int, int]):
    """Make a image buffer in the style the cameras might return

    This is intended to be a ``RGB888`` encoding, so the size/shape
    isn't what most people are used to for images in ``numpy`` land.
    """
    w, h = shape
    img = np.zeros((h, w, FAKE_CHANNELS), dtype=np.uint8)

    img[:, : w // 3, 0] = 255
    img[:, w // 3 : 2 * w // 3, 1] = 255
    img[:, 2 * w // 3 :, 2] = 255
    return img


class FakeCompletedRequest(CompletedRequest):
    def __init__(self, config: CameraConfig, metadata: Dict[str, Any]):
        self.config = config
        self.completion_time = time.time()
        self._metadata = metadata
        self._metadata["SensorTimestamp"] = int(
            (self.completion_time - 1.0) * 1_000_000_000
        )

    def acquire(self):
        pass

    def release(self):
        pass

    def get_camera_config(self) -> CameraConfig:
        """Fetch the configuration for the named stream."""
        return self.config

    def get_buffer(self, name: str) -> np.ndarray:
        """Make a 1d numpy array from the named stream's buffer."""
        size = self.config.get_stream_config(name).size
        return make_fake_image(size).flatten()

    def get_metadata(self) -> Dict[str, Any]:
        """Fetch the metadata corresponding to this completed request."""
        return self._metadata


class FakeCamera(RequestMachinery):
    def __init__(self, camera_num: int = 0, tuning=None) -> None:
        super().__init__()
        self._t = Thread(target=lambda: None, daemon=True)
        self._t.start()
        self._t.join()
        self._abort = Event()

        self.sensor_resolution = FAKE_SIZE
        self.sensor_format = FAKE_FORMAT
        self.camera_config = None
        self.camera_ctrl_info = {
            "AeEnable": 0,
            "AnalogueGain": 1.0,
            "DigitalGain": 1.0,
            "AwbEnable": 0,
            "ColourCorrectionMatrix": [1, 0, 0, 0, 1, 0, 0, 0, 1],
            "ColourGains": (2.5220680236816406, 1.8971731662750244),
            "ColourTemperature": 4000,
            "ExposureTime": 10000000,
            "FrameDurationLimits": (33333, 33333),
            "NoiseReductionMode": 0,
        }
        self.controls = Controls(self, self.camera_ctrl_info)

        self.config = CameraConfig(
            self,
            "still",
            1,
            controls=self.controls,
            transform=libcamera.Transform(),
            color_space=libcamera.ColorSpace.Sycc(),
            main=StreamConfig(size=FAKE_SIZE, format=FAKE_FORMAT, stride=FAKE_STRIDE),
        )

    def _run(self):
        while not self._abort.wait(self.controls.FrameDurationLimits[0] / 1000000):
            metadata = self.controls.make_dict()

            metadata.update(
                {
                    "AeLocked": False,
                    "FocusFoM": 93,
                    "FrameDuration": 24994,
                    "Lux": 330.6990051269531,
                }
            )
            request = FakeCompletedRequest(self.config, metadata)
            self.add_completed_request(request)
            self.process_requests()

    def configure(self, config: CameraConfig) -> None:
        self.camera_config = config
        self.controls.set_controls(config.controls)

    @property
    def info(self) -> CameraInfo:
        return CameraInfo(
            id="fake",
            model="Fake Camera",
            size=FAKE_SIZE,
            location="Nowhere",
            rotation=1,
        )

    @property
    def camera_controls(self):
        return {}

    def start_runloop(self):
        pass

    def stop_runloop(self):
        pass

    def start(self) -> None:
        self._t = Thread(target=self._run, daemon=True)
        self._abort.clear()
        self._t.start()

    def stop(self) -> None:
        self._abort.set()
        self._t.join()

    def close(self) -> None:
        if self._t.is_alive():
            self.stop()

    def switch_mode(self, camera_config: CameraConfig) -> TypedFuture[CameraConfig]:
        self.configure(camera_config)
        future = Future()
        future.set_result(camera_config)
        return future

    # TODO(meawoppl) - Kill methods below here
    def set_controls(self, controls: Dict[str, Any]) -> None:
        self.controls.set_controls(controls)

    def camera_configuration(self) -> CameraConfig:
        return self.camera_config
