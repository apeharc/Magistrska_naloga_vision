# Importing all the libraries
import cv2 as cv
from picamera2 import Picamera2
import time


#Start the camera with the default camera number and show the preview
picam2 = Picamera2()
# Create a still configuration for the camera which is used to capture the image in high resolution
capture_config = picam2.create_still_configuration()
picam2.start(show_preview=True)

while True:
    # Read a frame from the camera and store it in the variable frame and store the return value in ret
    frame = picam2.switch_mode_and_capture_array(capture_config, "image.jpg")
    # Display the frame in a window named 'Camera'
    cv.imshow('Camera', frame)
    # Check if the key 'q' is pressed and break the loop if the key 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all the windows
picam2.stop()
cv.destroyAllWindows()