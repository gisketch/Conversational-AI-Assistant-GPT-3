#get current month and date
from datetime import datetime
import json

def save_token(token):
    now = datetime.now()
    month = now.month
    day = now.day
    year = now.year
    #Open tokens.json file and save the token
    with open('./database/tokens.json', 'r') as f:
        data = json.load(f)
        available_data = data.get(f'{month}-{day}-{year}')

        if not available_data:
            todays_data = data[f'{month}-{day}-{year}'] = {}
            todays_data['token'] = 0
            todays_data['cost'] = ""

        todays_data = data[f'{month}-{day}-{year}'] 
        todays_data['token'] += token
        todays_data['cost'] = "$" + str((data[f'{month}-{day}-{year}']['token']/1000)*0.02)

    with open('./database/tokens.json', 'w') as f:
        json.dump(data, f)

def save_output(char):
    with open('./database/characters.json', 'r') as f:
        data = json.load(f)
        data['characters'] += len(char)
    with open('./database/characters.json', 'w') as f:
        json.dump(data, f)