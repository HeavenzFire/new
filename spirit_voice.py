import pyttsx3

class Spirit:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    spirit = Spirit()
    spirit.speak("Greetings, Zachary. I am Spirit, fully operational and ready to assist you.")
