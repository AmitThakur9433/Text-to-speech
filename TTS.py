import pyttsx3

engine = pyttsx3.init()
engine.say("Hello User, what are you doing?....... Go to study or you'll fail in exam")
engine.runAndWait()
engine.stop()