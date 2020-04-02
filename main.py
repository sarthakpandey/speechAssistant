import speech_recognition as sr
import webbrowser
import playsound
import time
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def recordAudio(ask=False):
    with sr.Microphone() as source:
        if(ask):
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I was unable to recognize that')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en-us', slow=False)
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Karen')
    if 'what time is it' in voice_data:
        speak(time.ctime())
    if 'search' in voice_data:
        search = recordAudio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    if 'location' in voice_data:
        location = recordAudio('Which location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        speak('bye bye then')
        exit()


time.sleep(1)
speak('How can I help you?')
while(1):
    voice_data = recordAudio()
    respond(voice_data)
