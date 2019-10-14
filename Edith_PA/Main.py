import pyttsx3 as tts
import datetime as dt
import speech_recognition as sr
from django.utils.datetime_safe import strftime
from spacy
import spacy

engine = tts.init('sapi5');

def configure_voice():
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[0].id)

def speak(audio):
    configure_voice()
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            print("Say something!")
            r.adjust_for_ambient_noise(source)       
            audio = r.listen(source)
            audio_text = r.recognize_google(audio,language = 'en-in')
            #audio_text = r.recognize_sphinx(audio,language = 'en-in')
            
            print("user voice: "+audio_text)
            nlp_processor(audio_text)
        except sr.UnknownValueError:
            print("sorry, i dint understand! say again")
            speak("sorry, say that again please")
        except Exception as e:
            print(e)
            speak("sorry, say that again please")
def nlp_processor(text):
    nlp = spacy(en_core_web_sm)
    
def wishme():
    x = int(dt.datetime.now().hour)
    if x >=0 and x<12:
        speak("Good morning praveen! ")
    if x>=12 and x<17:
        speak("Good afternoon praveen")
    elif x>=17 and x<=19:
        speak("Good evening praveen")
    elif x>=19 and x<=23:
        speak("Welcome, praveen")    
 
 
def date():
    x = dt.datetime.now()
    date = "today is "+x.strftime("%A")+" "+x.strftime("%d")+" of "+x.strftime("%B")+" "+x.strftime("%Y")
    speak(date)

#date()
 
wishme()
speak("Edith, at your service!")
while True:
    listen()
    