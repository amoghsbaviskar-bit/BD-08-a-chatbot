import pandas as pd
import random
import requests
import webbrowser
import wikipedia
import pygame
import time
from datetime import datetime


pygame.mixer.init()
beep = pygame.mixer.Sound("sounds/beep.wav")
boop = pygame.mixer.Sound("sounds/boop.wav")
option1 = pygame.mixer.Sound("sounds/option1.wav")
option2 = pygame.mixer.Sound("sounds/option2.wav")
option3 = pygame.mixer.Sound("sounds/option3.wav")
option4 = pygame.mixer.Sound("sounds/option4.wav")
option5 = pygame.mixer.Sound("sounds/option5.wav")
option6 = pygame.mixer.Sound("sounds/option6.wav")
option7 = pygame.mixer.Sound("sounds/option7.wav")


data = pd.read_excel("bd08_data.xlsx")

option_sounds = [option1, option2, option3, option4, option5, option6, option7]

print("THIS PROGRAM IS A MULTIPURPOSE CHAT BOT")

def play_sequence(sequence):
    for s in sequence:
        if s.lower() == "beep":
            beep.play()
        elif s.lower() == "boop":
            boop.play()
        time.sleep(0.3)  
        
        
def play_brain_sound():

    random.choice(option_sounds).play()

def math_brain(user_san):
    play_brain_sound()
    print("BD-08 : SURE GIVE ME AN EQUATION LIKE (2+3 or 8-9)")
    eq = input(f"{current_datetime} user: ")
    try:
        result = eval(eq)
        print(f"BD-08 : THE ANSWER IS {result}")
        
    except:
        print("BD-08 : Oops I COULDNT CALCULATE THAT")
        

def joke_brain(user_san):
    play_brain_sound()
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data_joke = response.json()
    print(f"BD-08 : {data_joke['setup']} ... {data_joke['punchline']}")

def wiki_brain(user_san):
    play_brain_sound()
    try:
        summary = wikipedia.summary(user_san, sentences=3)
        print(f"BD-08 : {summary} DO YOU NEED ANYTHING ELSE FEEL FREE TO MENTION")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"BD-08 : YOUR QUERY IS AMBIGUOUS DID YOU MEAN: {e.options[:5]}?")
    except wikipedia.exceptions.PageError:
        print("BD-08 : SORRY I COULDNT FIND ANYTHING ON THAT TOPIC")

def web_brain(user_san):
    websites = {
        "youtube": "https://www.youtube.com",
        "spotify": "https://open.spotify.com",
        "google":  "https://www.google.com"
    }
    for site in websites:
        if site in user_san.lower():
            play_brain_sound()
            print(f"BD-08 : OPENING {site.upper()} FOR USER ...")
            webbrowser.open(websites[site])
            return True
    return False

def weather_brain(user_san):
    play_brain_sound()
    API_KEY = "YOUR_API_KEY_HERE"
    BASE_URL = "http://api.weatherapi.com/v1/current.json"
    print("BD-08 : WHICH CITY DO YOU WANT THE WEATHER FROM ?")
    city = input(f"{current_datetime} user: ")
    params = {
        "key": API_KEY,
        "q": city
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data_w = response.json()
            play_brain_sound()
            print(f"BD-08 : WEATHER IN {city} --> {data_w['current']['condition']['text']}, {data_w['current']['temp_c']}°C")
        else:
            print("Error fetching weather:", response.status_code)
    except:
        play_brain_sound()
        print("BD-08 : COULD NOT FETCH WEATHER RIGHT NOW")
def quote_brain(user_san):
    play_brain_sound()
    Quote_Type = input("BD-08 : WHAT QUOTE DO YOU NEED ? -->")
    response = requests.get("https://thequoteshub.com/api/[Quote_Type]")
    data_quote = response.json()
    print(f"BD-08 : {data_quote['text']} -- {data_quote['author']}")
    
while True:
    current_datetime = datetime.now()
    user_san = input(f"{current_datetime} user: ")
    found = False
    if "bye" in user_san or "see ya" in user_san:
        play_brain_sound()
        print("BD-08 : BYE BYE!!")
        break


    if "calculate" in user_san or "calc" in user_san or "math" in user_san:
        math_brain(user_san)
        found = True
    elif "joke" in user_san or "tell me a joke" in user_san:
        joke_brain(user_san)
        found = True
    elif "define" in user_san or "what is " in user_san:
        query = user_san.lower().replace("define","").replace("what is","").strip()
        wiki_brain(query)
        found = True
    elif "open " in user_san:
        if web_brain(user_san):
            found = True
    elif "what is the weather" in user_san or "weather" in user_san:
        weather_brain(user_san)
        found = True
    elif "quote" in user_san or "give me a quote" in user_san:
        quote_brain(user_san)
        found = True

    if not found:
        for _, row in data.iterrows():
            keywords = [k.strip().lower() for k in row['User Inputs'].split(',')]
            if any(keyword in user_san.lower() for keyword in keywords):
                responses = [cell for cell in row[1:] if str(cell) != 'nan']
                response = random.choice(responses)
                print(f"BD-08: {response}")
               
                if "Sequence" in data.columns:
                    seq_val = str(row["Sequence"])
                    if seq_val.lower() != "nan":
                        seq_list = seq_val.split(",")
                        play_sequence(seq_list)
                found = True
                break
    if not found:
        print("BD-08: DIDN'T HEAR U WRITE\nTRY WRITING AGAIN")    