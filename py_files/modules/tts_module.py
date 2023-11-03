from gtts import gTTS
import os


CASHE = {}
MP3_PATH = 'F:/Projects/PycharmProjects/WordBook/mp3_cashe/{}.mp3'


def speak(word: str):
    if word not in CASHE:
        tts = gTTS(word, lang='en')
        tts.save(MP3_PATH.format(word))
        CASHE[word] = MP3_PATH.format(word)
    os.system(f'afplay {MP3_PATH.format(word)}')


