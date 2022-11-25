import speech_recognition as sr
import gtts
from playsound import playsound
import os
from datetime import datetime
from notion import NotionClient

r = sr.Recognizer()
notion_token = "secret_Dc3JH1XmlbTMlNF7KHqGCJkjX8WTZV9reBHgQIyT3GY"
database_id = "bdeb7b15d89247ebaaebe76126633b84"

ACTIVATION_COMMAND = "hey ambrose"

def get_audio():
    with sr.Microphone() as source:
        print("Say something")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError:
        print("could not request results from API")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("could not play sound")



if __name__ == "__main__":

    while True:
        a = get_audio()
        command = audio_to_text(a)

        if ACTIVATION_COMMAND in command.lower():
            print("activate")
            play_sound("What can I do for you at this time?")

            note = get_audio()
            note = audio_to_text(note)

            if note:
                play_sound(note)

                
