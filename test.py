import pyttsx3
# Initialize the library
engine = pyttsx3.init()
# specify the text you want to listen
text = "Wear mask, sanitize, social distance and be safe. Happy Thanksgiving!"
engine.say(text)
# Flush the say() queue to play the audio
engine.runAndWait()
