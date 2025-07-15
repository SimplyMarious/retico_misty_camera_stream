# Misty Camera Streaming with Retico Framework

## Overview

This project integrates the Misty robot's camera streaming capabilities with the Retico framework for incremental processing. The `MistyCameraStreamModule` streams video from the Misty robot, and the `ScreenModule` displays the video feed. The project demonstrates how to use Retico modules to process and display real-time video streams.

## Recommended Python Version

It is recommended to use **Python 3.9** for this project to ensure compatibility with all dependencies.

## Installation Guide

Follow these steps to set up the project:

1. **Clone the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/SimplyMarious/retico-misty-camera-stream.git retico_misty_camera_stream
   cd retico_misty_camera_stream
   ```

2. **Install Python Requirements**
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: For `retico-vision`, follow these steps:
   - Clone the `retico-vision` repository:
     ```bash
     git clone https://github.com/retico-team/retico-vision.git
     ```
   - Add the path to the cloned repository to your `PYTHONPATH` environment variable:
     - For Windows (PowerShell):
       ```powershell
       $env:PYTHONPATH="path\to\retico-vision;$env:PYTHONPATH"
       ```
     - For Linux bash:
       ```bash
       export PYTHONPATH=/path/to/retico-vision:$PYTHONPATH
       ```
   Replace `path\to\retico-vision` or `/path/to/retico-vision` with the actual path where you cloned the repository.

3. **Set Up the Environment**
   Ensure that the Misty robot is connected to the same network and note its IP address.

## Example Usage

The following example demonstrates how to use the project to stream video from the Misty robot and display it on the screen:

```python
import retico_misty_camera_stream.retico_core.network as network
from retico_screen import ScreenModule
from retico_misty_camera_stream.misty_camera_stream_module import MistyCameraStreamModule

# Initialize the Misty camera module with the robot's IP and desired settings
misty_camera = MistyCameraStreamModule(ip="10.10.2.112", res_width=1280, res_height=960, framerate=20)

# Initialize the screen module to display the video feed
screen = ScreenModule()

# Subscribe the screen module to the Misty camera module
misty_camera.subscribe(screen)

# Start the Retico network
network.run(misty_camera)
print("Running the Misty camera")

# Wait for user input to stop the network
input()

# Stop the Retico network
network.stop(misty_camera)
```

### Steps to Run the Example
1. Replace `10.10.2.112` with the IP address of your Misty robot.
2. Run the script:
   ```bash
   python main.py
   ```
3. Press `Ctrl+C` or provide input to stop the streaming.

## License
This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.

## Acknowledgments
- **Retico Framework**: For providing the modular framework for incremental processing.