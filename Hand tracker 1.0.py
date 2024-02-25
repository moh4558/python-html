import cv2
import mediapipe as mp


# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

    # If hands are detected, extract landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for point in hand_landmarks.landmark:
                # Extract landmark coordinates
                x, y, z = int(point.x * frame.shape[1]), int(point.y * frame.shape[0]), int(point.z * frame.shape[1])

                # Draw a circle at each landmark position
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Display the frame
    cv2.imshow("Hand Tracking", frame)
    
  # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
