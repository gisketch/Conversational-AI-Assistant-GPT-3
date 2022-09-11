
import pyttsx3

class Voice:

    def __init__ (self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 190)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)

    def talk(self,text):
        self.engine.say(text)
        self.engine.runAndWait()