from gtts import gTTS
import os
from playsound import playsound
import inspect


def tts_it(text):
    tts = gTTS(text=text, lang="it")
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    tts.save("voice.mp3")
    mp3File = "voice.mp3"
    voice_file = path + '\\' + mp3File
    playsound(voice_file)
    os.remove(mp3File)
