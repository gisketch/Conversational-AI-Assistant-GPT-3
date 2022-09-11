import pyaudio
import speech_recognition as sr
import gpt
import keyboard
import recorder as rec
# from deepmultilingualpunctuation import PunctuationModel
import remove_memory
from play_vid import Video_Player
from clips import Clips
import voice
import playsound
import os

#OUTPUT AUDIO
def talk(text):
    voice.talk(text)
    video_player.change(Clips.talking())
    playsound.playsound('./temp/temp_audio2.mp3', True)
    os.remove('./temp/temp_audio2.mp3')

audio = pyaudio.PyAudio()

#Speech_Recognition requirements
r = sr.Recognizer()
r.energy_threshold = 4000 #Adjust value depending on microphone
r.dynamic_energy_threshold = True

#Punctuation Model #00FFFF USE IF ABLE TO USE
# punc_model = PunctuationModel()

#MAKE A CONFIGURATION, manual or automatic

#    _____                 __  __                                 
#   / ____|               |  \/  |                                
#  | |     ___  _ __ ___  | \  / | ___ _ __ ___   ___  _ __ _   _ 
#  | |    / _ \| '__/ _ \ | |\/| |/ _ \ '_ ` _ \ / _ \| '__| | | |
#  | |___| (_) | | |  __/ | |  | |  __/ | | | | | (_) | |  | |_| |
#   \_____\___/|_|  \___| |_|  |_|\___|_| |_| |_|\___/|_|   \__, |
#                                                            __/ |
#                                                           |___/ 

core_prompt= """
The following is a conversation with a personal AI assistant. The assistant is helpful, creative, clever, funny, and very friendly.\n 

Some information about the AI:

- Is created by an Electronics Engineering student named "Ghegi" for his thesis
- Programmed in Python and powered by OpenAI's GPT-3
- AI is nicknamed "Zelda" inspired by the game "The Legend of Zelda"
- ZELDA also stands for Zealous Electronics Lifeform Designed for Assistance
- Is built on a fine-tuned model of OpenAI GPT-3 built to have human-like conversations

Core features:

- Talks like a human.
- Can get today's weather data.

Limitations:

- Short-term memory (30 back to back conversations)
- Requires internet
- Expensive (hardware limitations)

(IMPORTANT!!! Zelda does not repeat the same dialogue. She will say the same things but in a different way each time.)
<--The following is a continuation of their previous conversation-->
\n
"""

###############################################################

voice = voice.GTTS_Voice()
video_player = Video_Player(Clips.idle()) #initialize

#FF5555 NOTE!! Improve introductions
global new_prompt

with open('conversation.txt','r') as myfile:
    new_prompt = myfile.read()

def ai_reply(input):
    
    global new_prompt #This is to grab the new_prompt variable from outside the scope
    
    #If char count of the prompt is more than 4500, remove memory, THIS IS TO SAVE TOKENS
    if len(new_prompt) > 4500:
        new_prompt = remove_memory(new_prompt)
        print("Removed a memory")

    #Combine the new prompt with the user's input
    prompt = new_prompt + input +"\nZelda:"

    print("\nGenerating a reply...")
    #Grab an output by inputting the new_prompt and the core_memory to the default GPT-3 completion
    output = gpt.default(prompt, core_prompt)

    #Remove core_memory to new_prompt for the conversation
    new_prompt = new_prompt.replace(core_prompt,"")
    new_prompt = prompt + output + "\nHuman: "

    with open('conversation.txt','w') as myfile:
        myfile.write(new_prompt)

    # print("Sentiment: " + gpt.sentiment(output))
    print("Message: " + output) #Print Zelda's reply to the console
    talk(output) #TTS the reply
    video_player.change(Clips.idle())

while True:
    #Record audio when pressing q
    print("Press q to record")
    keyboard.wait("q")

    #CHANGE VIDEO
    video_player.change(Clips.listen_transition())

    transcribed_text = rec.record_audio(audio,r,sr)

    video_player.change(Clips.thinking()) #TODO: Move after pressing E
    #99ff9933 For testing
    # transcribed_text = input("Human: ") 
    #TODO: Enable for punctuation
    # recased_text = gpt.punctuate(transcribed_text)
    print("Human: " + transcribed_text)

    ai_reply(transcribed_text)

    
        
