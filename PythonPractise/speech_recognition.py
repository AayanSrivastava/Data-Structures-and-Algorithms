import pyttsx3
import speech_recognition as sr
from speech_recognition import Recognizer

# initialize the speech recognition and text-to-speech synthesis engines
r = Recognizer()
engine = pyttsx3.init()

# define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define a function to recognize voice commands
def recognize():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
    except sr.RequestError:
        speak("Sorry, I couldn't connect to the Internet.")

# define a function to perform the given task
def perform_task(task):
    if "open" in task:
        if "browser" in task:
            speak("Opening web browser...")
            # code to open a web browser
    elif "play" in task:
        if "music" in task:
            speak("Playing music...")
            # code to play music
    elif "check" in task:
        if "weather" in task:
            speak("Checking weather...")
            # code to check the weather
    else:
        speak("Sorry, I don't know how to do that.")

# main program loop
while True:
    command = recognize()
    if command:
        perform_task(command)
