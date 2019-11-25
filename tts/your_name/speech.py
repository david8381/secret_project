from gtts import gTTS
import os, record_wav as rw, speech_recognition as sr

def record(file_name):
    rw.record_to_file(file_name)


def say(mytext):
    print(mytext)
    myobj = gTTS(text=mytext, lang='en', slow=False)
    myobj.save('to_say.mp3')
    os.system("afplay {}".format('to_say.mp3'))


def stt(file_name):
    r = sr.Recognizer()

    file = sr.AudioFile(file_name)
    with file as source:
        audio = r.record(source)

    text = r.recognize_google(audio)
    return text


def s_input(prompt=""):
    if prompt != "":
        say(prompt)
    record("input.wav")
    return stt("input.wav")


if __name__ == '__main__':
    print("Example program")
    text = s_input("What is your name?")
    say("Hello, {}".format(text))
