
import pyttsx3
from gtts import gTTS
import ffmpy



class Voice:

    def __init__ (self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)

    def talk(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

class GTTS_Voice:

    def talk(self, text):
        tts = gTTS(text, lang='en', tld='co.uk')
        tts.save("./temp/temp_audio.mp3")    
        ff = ffmpy.FFmpeg(inputs={"./temp/temp_audio.mp3": None}, outputs={"./temp/temp_audio2.mp3": ["-filter:a", "atempo=1.3"]})
        ff.run()