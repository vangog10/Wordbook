import pyttsx3


def speak(word: str):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


