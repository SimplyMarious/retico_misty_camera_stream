import retico_core.network as network
from retico_screen import ScreenModule
from misty_camera_stream_module import MistyCameraStreamModule


misty_camera = MistyCameraStreamModule(ip="10.10.2.112", rtsp_port=1936, res_width=1280, res_height=960, framerate=20)
screen = ScreenModule()

misty_camera.subscribe(screen)

network.run(misty_camera)
print("Running the Misty camera")

input()

network.stop(misty_camera)