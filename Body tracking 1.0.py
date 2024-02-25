import cv2
import numpy as np

# Load the pre-trained body detection model
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Open a video capture object (you can also use cv2.VideoCapture(0) for webcam)
cap = cv2.VideoCapture('path/to/your/video.mp4')

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect bodies in the frame
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Body Tracking', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
