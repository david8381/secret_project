from gtts import gTTS 
import os
#import vlc
#import playsound

mytext = 'Alert. Alert. Computer failure'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("welcome.wav") 

os.system("afplay welcome.wav")


#os.system("mpg321 welcome.mp3") 

#p = vlc.MediaPlayer("welcome.mp3")
#p.play()

#playsound.playsound("welcome.mp3", True)
