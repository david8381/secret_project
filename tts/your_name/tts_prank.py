import text_and_speech as tas
from time import sleep

length = int(input("How long in seconds"))
message = input("Message")
seconds = 0

while seconds < length:
    sleep(1)
    print(seconds,"/",length)
    seconds+=1

while True:
    tas.say(message)
    time.sleep(1)
