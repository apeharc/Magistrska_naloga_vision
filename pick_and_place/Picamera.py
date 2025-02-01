# Importing all the libraries
from picamera2 import Picamera2
import time

#Start the camera with the default camera number and show the preview
picam2 = Picamera2()
# Create a still configuration for the camera which is used to capture the image in high resolution
capture_config = picam2.create_still_configuration()
picam2.start(show_preview=True)
# Wait for 1 second then take a picture
time.sleep(1)
# Switch the camera mode to 'main' and capture an array of the image
array = picam2.switch_mode_and_capture_array(capture_config, "main")