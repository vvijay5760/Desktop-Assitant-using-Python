import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Taking Voice from my system

engine = pyttsx3.init() # to access the voice property of the OS. 'sapi5' is the initialization parameter on windows
voices = engine.getProperty('voices')
# print(voices)
# print(type(voices))

# print(len(voices))

# engine.setProperty('voice',voices[142].id) # to set the voice type
engine.setProperty('rate',150)

# Text to Speech Function
def speak(test):
    """
    This function is for text to speech conversion
    Args: text(_type_): string
    """
    engine.say(test)
    engine.runAndWait()

# speak("Hello I am a programmer, How are you?")

# Speech to Text Function
def takeCommand():
    """
    This function will recognize voice and returns text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-US")
            print(f"User said:{query}\n")

        except Exception as e:
            print("Voice couldn't be recognized. Please say it again")
            return None
    return query



if __name__ == "__main__":
    print("Welcome to the Speech Recognition Program")
    print("-----------------------------------------")
    query = takeCommand().lower()
    #print(query)
    #speak(query)

    if "wikipedia" in query:
        query = query.replace("wikipedia","")
        t = wikipedia.summary(query,sentences = 2)
        speak("According to Wikipedia")
        print(t)