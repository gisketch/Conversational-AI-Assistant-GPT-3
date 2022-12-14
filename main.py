import pyaudio
import speech_recognition as sr
import gpt
import keyboard
import recorder as rec
# from deepmultilingualpunctuation import PunctuationModel
from remove_memory import remove_memory
from play_vid import Video_Player
from clips import Clips
import voice
from playsound import playsound
import os
import get_weather
from record_token import save_output

#OUTPUT AUDIO
def talk(text):
    voice.talk(text)
    video_player.change(Clips.talking())
    playsound('./temp/temp_audio.mp3')
    os.remove('./temp/temp_audio.mp3')
    # playsound.playsound('./temp/temp_audio2.mp3', True)
    video_player.change(Clips.idle())

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

<--The following is a continuation of their previous conversation-->
\n
"""

###############################################################

voice = voice.Polly_Voice()
video_player = Video_Player(Clips.boot()) #initialize

#FF5555 NOTE!! Improve introductions
global new_prompt

with open('./database/conversation.txt','r',encoding="utf-8") as myfile:
    new_prompt = myfile.read()

def ai_reply(input):
    
    global new_prompt #This is to grab the new_prompt variable from outside the scope
    
    #If char count of the prompt is more than 2000, remove memory, THIS IS TO SAVE TOKENS
    if len(new_prompt) > 2000:
        new_prompt = remove_memory(new_prompt)
        print("Removed a memory")

    #Combine the new prompt with the user's input
    prompt = new_prompt + input +"\nZelda:"

    print("\nGenerating a reply...")

    #Grab an output by inputting the new_prompt and the core_memory to the default GPT-3 completion
    if 'weather' in input.lower():
        weather_info = gpt.weather(input)
        if weather_info["Output"] == True:
            print(weather_info)
            weather_info_2 = get_weather.get_weather_data(weather_info["Location"], "today")
            if 'error' in weather_info_2:
                output = gpt.weather_error_reply()
            else:
                output = gpt.weather_reply(weather_info_2)
        else:
            output = gpt.default(prompt, core_prompt)
    else:
        output = gpt.default(prompt, core_prompt)

    #Remove core_memory to new_prompt for the conversation
    new_prompt = new_prompt.replace(core_prompt,"")
    new_prompt = prompt + output + "\nHuman: "

    with open('./database/conversation.txt','w', encoding="utf-8") as myfile:
        myfile.write(new_prompt)

    # print("Sentiment: " + gpt.sentiment(output))
    print("Message: " + output) #Print Zelda's reply to the console
    talk(output) #TTS the reply
    save_output(output)

def weather_ask(input):
    talk(gpt.weather(input))

while True:
    #Record audio when pressing q
    print("Press q to record")
    keyboard.wait("q")

    #CHANGE VIDEO
    video_player.change(Clips.listening())

    transcribed_text = rec.record_audio(audio,r,sr)

    video_player.change(Clips.thinking()) #TODO: Move after pressing E
    #99ff9933 For testing
    # transcribed_text = input("Human: ") 
    #TODO: Enable for punctuation
    recased_text = gpt.punctuate(transcribed_text)
    print("Human: " + recased_text)
    
    ai_reply(recased_text)

    
        
