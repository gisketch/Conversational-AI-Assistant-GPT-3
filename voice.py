
import pyttsx3
from gtts import gTTS
import ffmpy
import boto3
from dotenv import load_dotenv
import os

load_dotenv()

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
    
class Polly_Voice:
    
    def __init__(self):
        self.polly_client = boto3.Session(
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),                     
                aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
                region_name='us-east-1').client('polly')

    def talk(self, text):
        response = self.polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = text,
                Engine = 'neural')

        file = open('speech.mp3', 'wb')
        file.write(response['AudioStream'].read())
        file.close()