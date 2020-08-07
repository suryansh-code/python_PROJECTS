import playsound
import speech_recognition as sr
from gtts import gTTS


# making a folder tat save each and every file here that the pyro will speak
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

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

speak('hello how are you, welcme to the text game,the game starts with you are struct in a jungle ,what will you do next,go towards river or jungle')
while True:
    if jungle in text:
        speak('ohh shit you are dead,because lions are too hungry')
        break
    elif river in text:
        speak('nice move carry on you  escape from jungle ,,,but you have to make a choice which vehicle you choose plane or ship ')
        if plane in text:
            speak('you escape congrets')
            break
        elif ship in text:
            speak('ohh shit!!!! the ship blast and drawn')
            break
        else:
            speak('wrong command')
            break
    else:
        speak('wrong command')
        break

