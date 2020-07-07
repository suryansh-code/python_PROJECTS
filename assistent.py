import speech_recognition as sr
import time
import playsound
from gtts import gTTS



# making a folder tat save each and every file here that the pyro will speak
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

seconds = 1545925769.9618232



# a function which takes the user audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(audio)
            print(said)

        except Exception as e:
            speak("sorry i am having problem understaning this ")

    return said.lower()


text = get_audio()

if 'hello' in text:
    speak('hi,how can i help you')
if 'what is your name' in text:
    speak('the word you just said pyro[];l,programed by suryansh')
if 'what can you do' in text:
    speak('bunch of things')

if 'time' in text:
    speak(time.ctime(seconds))
if 'who is alexa' in text:
    speak('alexa the worst artificial intelligence ')
