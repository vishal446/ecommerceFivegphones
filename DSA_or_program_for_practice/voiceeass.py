import pyttsx3
import speech_recognition as sp
import webbrowser
import datetime
import pyjokes

def speechtext():
    recognizer=sp.Recognizer() #catches voice though microphone
    with sp.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) #reome backgournd noise 
        audio=recognizer.listen(source)
        try:
            print("recognzing...")
            data=recognizer.recognize_google(audio)
            print(data)
        except sp.UnknownValueError:
            print("Could't not understand!")
speechtext()