#making a simple jarvis programe

import wikipedia
import pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

#taking up the voice property
engine=pyttsx3.init('sapi5')


#tain the sample of vice of ai ie david or zira
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#the function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#the function which greet me according to the givin time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        
    elif hour>=12 and hour<=18:
        speak("good Afternoon")
    
    else:
        speak("good evening")

    speak("hellow  my name is hinata. how can i help you?")
    
#the function takeCommand take our voice as input from microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio =r.listen(source)
        
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")
        
    except Exception as e:
        speak("can you repeat thae again please")
        return "NONE"
    
    return query

if __name__=='__main__':
    wishMe()
    run=True
    while run:
        query=takeCommand().lower()
        
        if "wikipedia" in query:
            speak('searching on wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif "what can you do" in query:
            speak("i can play music ,open websites ,and , apps and many more")
    
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com") 
            
        elif "pause" in query:
            run=False
        
        elif "how are you" in query:
            speak("i am fine . thanks for asking")
        
        elif ("tell me about yourself" )in query:
            speak("hellow my name is hinata,i am an artificial intelligence assistent created as a group project , i am designed using python")
        

