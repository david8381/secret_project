import speech_recognition as sr

r = sr.Recognizer()

alert = sr.AudioFile('welcome.wav')
with alert as source:
    audio = r.record(source)

text = r.recognize_google(audio)

print(text)
