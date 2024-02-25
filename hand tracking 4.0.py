import cv2
import mediapipe as mp
import sounddevice as sd
import soundfile as sf
import numpy as np
import math

class HandVolumeController:
    def __init__(self):
        # Initialize mediapipe hands module
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

        # Open a connection to the webcam
        self.cap = cv2.VideoCapture(0)
        self.screen_width, self.screen_height = 1920, 1080  # Adjust to your screen resolution

        # Set initial volume
        self.initial_volume = 0.5  # Initial volume level (0.0 to 1.0)

        # Set volume step and interpolation factor (adjust as needed)
        self.volume_step = 0.05
        self.interpolation_factor = 0.5

        # Initialize variables for gesture recognition
        self.last_gesture = None
        self.gesture_frames = 0

    def detect_hand_gesture(self, hand_landmarks):
        thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]

        thumb_x, thumb_y = int(thumb_tip.x * self.screen_width), int(thumb_tip.y * self.screen_height)
        index_x, index_y = int(index_tip.x * self.screen_width), int(index_tip.y * self.screen_height)

        distance = math.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)
        return thumb_x, thumb_y, index_x, index_y, distance

    def set_volume(self, volume):
        try:
            # Generate a silent audio file
            data = np.zeros((44100, 2), dtype=np.float32)
            sf.write('silent.wav', data, 44100, 'PCM_24')

            # Play the silent audio file with the desired volume
            sd.play(data, 44100, device=None, volume=volume, blocking=True)

        except Exception as e:
            print(f"Error setting volume: {e}")

    def adjust_volume(self, target_volume, hand_landmarks):
        current_volume = self.initial_volume
        thumb_x, thumb_y, index_x, index_y, distance = self.detect_hand_gesture(hand_landmarks)

        interpolated_volume = (1 - self.interpolation_factor) * current_volume + self.interpolation_factor * target_volume

        # Perform volume adjustment only if the distance is small (gesture stability)
        if distance < 50:
            self.set_volume(interpolated_volume)

            # Set the current gesture
            self.last_gesture = "Volume Control"
            self.gesture_frames = 0

    def run(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    target_volume = self.initial_volume + (hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * self.screen_height - 100) / 10 * self.volume_step
                    self.adjust_volume(target_volume, hand_landmarks)

            # Display the current gesture on the frame
            if self.last_gesture:
                cv2.putText(frame, f"Gesture: {self.last_gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 255), 2)
                self.gesture_frames += 1

                # Reset gesture after a certain number of frames (adjust as needed)
                if self.gesture_frames > 30:
                    self.last_gesture = None
                    self.gesture_frames = 0

            # Display the frame
            cv2.imshow("Professional Hand Tracking for Volume Control", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close all windows
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        hand_volume_controller = HandVolumeController()
        hand_volume_controller.run()
    except Exception as e:
        print(f"An error occurred: {e}")
