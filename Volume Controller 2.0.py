import cv2
import numpy as np
import math
import pyautogui
import mediapipe as mp

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to calculate the distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to get thumb and index finger positions
def get_thumb_and_index_positions(hand_landmarks):
    thumb_x, thumb_y = hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y
    index_x, index_y = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y
    return thumb_x, thumb_y, index_x, index_y

# Function to smoothly transition between volumes
def smooth_volume_transition(current_volume, target_volume, smoothing_factor=0.1):
    return current_volume + smoothing_factor * (target_volume - current_volume)

# Function to recognize different hand gestures
def recognize_gesture(hand_landmarks):
    try:
        # Example: Check if the thumb is higher than the index finger for "thumbs up"
        if hand_landmarks.landmark[4].y < hand_landmarks.landmark[8].y:
            return "thumbs_up"
        # Add more gesture checks as needed...
        else:
            return "no_gesture"
    except IndexError as e:
        print(f"Error recognizing gesture: {e}")
        return "no_gesture"

# Function to confirm a gesture before triggering an action
def confirm_gesture(gesture, confidence_threshold=0.8):
    # Placeholder for confidence calculation, adjust as needed
    confidence = 0.9
    return confidence > confidence_threshold

# Function to control the volume based on hand position
def control_volume(hand_landmarks, current_volume):
    if hand_landmarks is None:
        print("Hand landmarks not found.")
        return current_volume
    
    try:
        thumb_x, thumb_y, index_x, index_y = get_thumb_and_index_positions(hand_landmarks)
        distance = calculate_distance(thumb_x, thumb_y, index_x, index_y)
        
        # Map the distance to the volume range (0-100)
        target_volume = np.interp(distance, [10, 200], [0, 100])
        
        # Smoothly transition between volumes
        smoothed_volume = smooth_volume_transition(current_volume, target_volume)
        
        # Confirm the gesture before adjusting the volume
        gesture = recognize_gesture(hand_landmarks)
        if confirm_gesture(gesture):
            if smoothed_volume > current_volume:
                pyautogui.press('volumeup', presses=int(smoothed_volume - current_volume))
            elif smoothed_volume < current_volume:
                pyautogui.press('volumedown', presses=int(current_volume - smoothed_volume))
        
        return smoothed_volume
    
    except Exception as e:
        print(f"Error in control_volume: {e}")
        return current_volume

# Main loop for capturing video frames
cap = cv2.VideoCapture(0)

# Initial volume value
current_volume = 50

while True:
    ret, frame = cap.read()

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to find hands
    try:
        results = hands.process(rgb_frame)

        # If hands are found, extract landmarks and call control_volume
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Call your control_volume function here with hand_landmarks
                current_volume = control_volume(hand_landmarks, current_volume)

                # Draw the hand landmarks on the frame (optional)
                mp_hands.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    except Exception as e:
        print(f"Error processing frame: {e}")

    # Display the frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
