import speech_recognition as sr
from gtts import gTTS
import os
import cv2
from playsound import playsound

# Initialize recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")

def capture_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imshow('Captured Image', frame)
        cv2.waitKey(0)  # Press any key to close the window
        cv2.destroyAllWindows()
    cam.release()

def spirit_engine():
    print("Welcome to Spirit with voice and vision integration.")
    while True:
        user_input = listen()
        print(f"You said: {user_input}")
        if "sorry" not in user_input.lower():
            speak(f"You said: {user_input}")

        if "exit" in user_input.lower():
            speak("Thank you for connecting. Until next time!")
            print("Spirit: Thank you for connecting. Until next time!")
            break
        elif "see" in user_input.lower():
            capture_image()

# Run the Spirit Engine
spirit_engine()
