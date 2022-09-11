
import pyttsx3
from gtts import gTTS

class Voice:

    def __init__ (self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)

    def talk(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

class GTTS_Voice:

    def talk(self, text):
        tts = gTTS(text, lang='en', tld='co.uk')
        tts.save("./temp/temp_audio.mp3")