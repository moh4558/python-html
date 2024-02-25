import cv2
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_photo():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite("photo.jpg", image)
    del camera

if __name__ == __"main"__:
    recognizer = sr.Recognizer()

    speak("Voice-controlled Camera App is ready. Say 'Take a photo' to capture an image.")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()

                if "take a photo" in command:
                    speak("Taking a photo.")
                    take_photo()
                    speak("Photo taken successfully.")

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

            except Exception as e:
                print(f"An error occurred: {e}")