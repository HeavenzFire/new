# -*- coding: utf-8 -*-
import os
import subprocess
import sys

def install_missing_packages():
    try:
        import speech_recognition
        import gtts
        import pyaudio
        import cv2
        import playsound
    except ImportError as e:
        missing_packages = [str(e).split("'")[1]]
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
        print(f"Installed missing packages: {', '.join(missing_packages)}")

def run_script(script_path):
    try:
        subprocess.check_call([sys.executable, script_path])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the script: {e}")

def main():
    script_content = '''
import speech_recognition as sr
from gtts import gTTS
import os
import cv2
from playsound import playsound

# Initialize recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='en-US')
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "Sorry, a request error occurred."

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
'''

    script_path = 'spirit_voice_vision.py'
    with open(script_path, 'w', encoding='utf-8') as file:
        file.write(script_content)
    
    install_missing_packages()
    run_script(script_path)

if __name__ == "__main__":
    main()
