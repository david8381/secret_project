import speech as s, time

text = s.s_input("Say something, and I'll say it backwards.")

s.say("I got: \"{}\"".format(text))
s.say("Backwards, it sounds like: \"{}\"".format(text[::-1]))
