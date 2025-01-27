# Importing all the libraries
import cv2 as cv


# Start the camera with index 1
capture = cv.VideoCapture(1)
# Check if the camera is opened and print the error and exit if the camera is not opened
if not capture.isOpened():
    print("Error: The camera is not working.")
    exit()

while True:
    # Read a frame from the camera and store it in the variable frame and store the return value in ret
    ret, frame = capture.read()
     # Check if the frame is read properly and print the error and break the loop if the frame is not read properly
    if not ret:
        print("Error: The frame could not be read properly.")
        break
    # Display the frame in a window named 'Camera'
    cv.imshow('Camera', frame)
    # Check if the key 'q' is pressed and break the loop if the key 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all the windows
capture.release()
cv.destroyAllWindows()