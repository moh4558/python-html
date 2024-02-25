import cv2
import mediapipe as mp
import pyautogui

# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

# Get screen width and height
screen_width, screen_height = pyautogui.size()

# Set initial volume
initial_volume = pyautogui.volumeInfo()["volume"]

# Set volume step (adjust as needed)
volume_step = 5

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
            # Extract coordinates of specific landmarks (adjust as needed)
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Get thumb and index finger tip positions
            thumb_x, thumb_y = int(thumb_tip.x * screen_width), int(thumb_tip.y * screen_height)
            index_x, index_y = int(index_tip.x * screen_width), int(index_tip.y * screen_height)

            # Draw circles at thumb and index finger tips
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)
            cv2.circle(frame, (index_x, index_y), 10, (0, 0, 255), -1)

            # Check if index finger is close to thumb (gesture for volume control)
            if abs(index_x - thumb_x) < 20 and abs(index_y - thumb_y) < 20:
                # Change the volume based on the thumb's y-coordinate
                new_volume = initial_volume + int((thumb_y - 100) / 10) * volume_step
                pyautogui.press("volumemute")  # Mute to prevent abrupt volume change
                pyautogui.press("volumedown")  # Move volume down
                pyautogui.press("volumemute")  # Unmute

                # Update initial volume for the next iteration
                initial_volume = new_volume

    # Display the frame
    cv2.imshow("Hand Tracking for Volume Control", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
