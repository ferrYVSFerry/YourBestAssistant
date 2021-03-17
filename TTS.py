from gtts import gTTS
import os
from playsound import playsound


def tts_it(text):
    tts = gTTS(text=text, lang="it")
    tts.save("1.wav")
    mp3File = "1.wav"
    playsound(mp3File)
    os.remove("1.wav")


if __name__ == "__main__":
    tts_it("ciao")
