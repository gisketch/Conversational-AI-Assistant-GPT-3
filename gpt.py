import openai
import json
import record_token
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('GPT_KEY')


# ##############################################
#       _       __            _ _   
#      | |     / _|          | | |  
#    __| | ___| |_ __ _ _   _| | |_ 
#   / _` |/ _ \  _/ _` | | | | | __|
#  | (_| |  __/ || (_| | |_| | | |_ 
#   \__,_|\___|_| \__,_|\__,_|_|\__|
#
 ################################################

def default(text, core_prompt):
        #Returns an object of the response from the completion API
    response = openai.Completion.create(
        model= "text-davinci-002", #USES THE TEXT-DAVINCI MODEL
        prompt = core_prompt + text,
        temperature=0.9,
        max_tokens=2048)
    
    #saves the number of tokens used
    tokens = ( len(core_prompt + text) + len(response.choices[0].text) ) / 4
    record_token.save_token(tokens)
    
    return response.choices[0].text
 
 ################################################
#                          _               _       
#                         | |             | |      
#   _ __  _   _ _ __   ___| |_ _   _  __ _| |_ ___ 
#  | '_ \| | | | '_ \ / __| __| | | |/ _` | __/ _ \
#  | |_) | |_| | | | | (__| |_| |_| | (_| | ||  __/
#  | .__/ \__,_|_| |_|\___|\__|\__,_|\__,_|\__\___|
#  | |                                             
#  |_|                                             
 #################################################

def punctuate(text):
    print("Punctuating...")

    prompt = """Fix punctuations.

<<|EXAMPLE|>>
{"Input": "hello what's the weather today"}
<<|OUTPUT|>>
{"Output": "Hello, what's the weather today?"}

<<|EXAMPLE|>>
{"Input": "hey jonathan lets go to the party"}
<<|OUTPUT|>>
{"Output": "Hey Jonathan, let's go to the party!"}

<<|EXAMPLE|>>
{"Input": """ + '"' + text + '"}\n<<|OUTPUT|>>\n'

    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt = prompt,
        temperature=0,
        max_tokens = 512,)
    output_object = json.loads(response.choices[0].text)

    #saves the number of tokens used
    tokens = ( len(prompt) + len(response.choices[0].text) ) / 4
    record_token.save_token(tokens)

    return output_object["Output"]

#################################################
#                  _   _                      _   
#                 | | (_)                    | |  
#   ___  ___ _ __ | |_ _ _ __ ___   ___ _ __ | |_ 
#  / __|/ _ \ '_ \| __| | '_ ` _ \ / _ \ '_ \| __|
#  \__ \  __/ | | | |_| | | | | | |  __/ | | | |_ 
#  |___/\___|_| |_|\__|_|_| |_| |_|\___|_| |_|\__|
#
#################################################

#TODO: if text is too long, return neutral
def sentiment(text):
    print("Identifying sentiment...")

    prompt = """Identify the sentiment of the input whether it's sad, happy, mad, scared, or neutral

<<|EXAMPLE|>>
{"Input": "my dog just died"}
<<|OUTPUT|>>
{"Output": "sad"}

<<|EXAMPLE|>>
{"Input": "happy birthday!"}
<<|OUTPUT|>>
{"Output": "happy"}

<<|EXAMPLE|>>
{"Input": """ + '"' + text + '"}\n<<|OUTPUT|>>\n'

    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        temperature=0,
        max_tokens = 256,)
    output_object = json.loads(response.choices[0].text)

    #saves the number of tokens used
    tokens = ( len(prompt) + len(response.choices[0].text) ) / 4
    record_token.save_token(tokens)

    return output_object["Output"]

#################################################
#                      _   _               
#                     | | | |              
#  __      _____  __ _| |_| |__   ___ _ __ 
#  \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|
#   \ V  V /  __/ (_| | |_| | | |  __/ |   
#    \_/\_/ \___|\__,_|\__|_| |_|\___|_|   
#
#################################################

def weather(text):
    print("Identifying if asking about the weather...")

    prompt = """Identify whether the person is asking about the weather today or not

<<|EXAMPLE|>>
{"Input": "what's the weather today?"}
<<|OUTPUT|>>
{"Output": true}

<<|EXAMPLE|>>
{"Input": "what's the weather tomorrow?"}
<<|OUTPUT|>>
{"Output": false}

<<|EXAMPLE|>>
{"Input": """ + '"' + text + '"}\n<<|OUTPUT|>>\n'

    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        temperature=0,
        max_tokens = 256,)
    output_object = json.loads(response.choices[0].text)

        #saves the number of tokens used
    tokens = ( len(prompt) + len(response.choices[0].text) ) / 4
    record_token.save_token(tokens)

    return output_object["Output"]