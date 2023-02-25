# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()

#Greet

from datetime import datetime


def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

import speech_recognition as sr
from random import choice
from utils import opening_text


def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]


import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_cmd():
    os.system('start cmd')

import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

{
  "ip": "117.214.111.199"
}

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

{
  "status": "ok",
  "totalResults": 38,
  "articles": [
    {
      "source": {
        "id": null,
        "name": "Sportskeeda"
      },
      "author": "Aniket Thakkar",
      "title": "Latest Free Fire redeem code to get Weapon loot crate today (14 October 2021) - Sportskeeda",
      "description": "Gun crates are one of the ways that players in Free Fire can obtain impressive and appealing gun skins.",
      "url": "https://www.sportskeeda.com/free-fire/latest-free-fire-redeem-code-get-weapon-loot-crate-today-14-october-2021",
      "urlToImage": "https://staticg.sportskeeda.com/editor/2021/10/d0b83-16341799119781-1920.jpg",
      "publishedAt": "2021-10-14T03:51:50Z",
      "content": null
    },
    {
      "source": {
        "id": null,
        "name": "NDTV News"
      },
      "author": null,
      "title": "BSF Gets Increased Powers In 3 Border States: What It Means - NDTV",
      "description": "Border Security Force (BSF) officers will now have the power toarrest, search, and of seizure to the extent of 50 km inside three newstates sharing international boundaries with Pakistan and Bangladesh.",
      "url": "https://www.ndtv.com/india-news/bsf-gets-increased-powers-in-3-border-states-what-it-means-2574644",
      "urlToImage": "https://c.ndtvimg.com/2021-08/eglno7qk_-bsf-recruitment-2021_625x300_10_August_21.jpg",
      "publishedAt": "2021-10-14T03:44:00Z",
      "content": "This move is quickly snowballing into a debate on state autonomy. New Delhi: Border Security Force (BSF) officers will now have the power to arrest, search, and of seizure to the extent of 50 km ins… [+4143 chars]"
    },
    {
      "source": {
        "id": "the-times-of-india",
        "name": "The Times of India"
      },
      "author": "TIMESOFINDIA.COM",
      "title": "5 health conditions that can make your joints hurt - Times of India",
      "description": "Joint pain caused by these everyday issues generally goes away on its own when you stretch yourself a little and flex your muscles.",
      "url": "https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/5-health-conditions-that-can-make-your-joints-hurt/photostory/86994969.cms",
      "urlToImage": "https://static.toiimg.com/photo/86995017.cms",
      "publishedAt": "2021-10-14T03:30:00Z",
      "content": "Depression is a mental health condition, but the symptoms may manifest even on your physical health. Unexpected aches and pain in the joints that you may experience when suffering from chronic depres… [+373 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "The Indian Express"
      },
      "author": "Devendra Pandey",
      "title": "Rahul Dravid likely to be interim coach for New Zealand series - The Indian Express",
      "description": "It’s learnt that a few Australian coaches expressed interest in the job, but the BCCI isn’t keen as they are focussing on an Indian for the role, before they look elsewhere.",
      "url": "https://indianexpress.com/article/sports/cricket/rahul-dravid-likely-to-be-interim-coach-for-new-zealand-series-7570990/",
      "urlToImage": "https://images.indianexpress.com/2021/05/rahul-dravid.jpg",
      "publishedAt": "2021-10-14T03:26:09Z",
      "content": "Rahul Dravid is likely to be approached by the Indian cricket board to be the interim coach for Indias home series against New Zealand. Head coach Ravi Shastri and the core of the support staff will … [+1972 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "CNBCTV18"
      },
      "author": null,
      "title": "Thursday's top brokerage calls: Infosys, Wipro and more - CNBCTV18",
      "description": "Goldman Sachs has maintained its 'sell' rating on Mindtree largely due to expensive valuations, while UBS expects a muted reaction from Wipro's stock. Here are the top brokerage calls for the day:",
      "url": "https://www.cnbctv18.com/market/stocks/thursdays-top-brokerage-calls-infosys-wipro-and-more-11101072.htm",
      "urlToImage": "https://images.cnbctv18.com/wp-content/uploads/2019/03/buy-sell.jpg",
      "publishedAt": "2021-10-14T03:26:03Z",
      "content": "MiniGoldman Sachs has maintained its 'sell' rating on Mindtree largely due to expensive valuations, while UBS expects a muted reaction from Wipro's stock. Here are the top brokerage calls for the day:"
    }
  ]
}

OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

{
    "coord": {
        "lon": 85,
        "lat": 24.7833
    },
    "weather": [
        {
            "id": 721,
            "main": "Haze",
            "description": "haze",
            "icon": "50d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 26.95,
        "feels_like": 26.64,
        "temp_min": 26.95,
        "temp_max": 26.95,
        "pressure": 1011,
        "humidity": 36
    },
    "visibility": 3000,
    "wind": {
        "speed": 2.57,
        "deg": 310
    },
    "clouds": {
        "all": 57
    },
    "dt": 1637227634,
    "sys": {
        "type": 1,
        "id": 9115,
        "country": "IN",
        "sunrise": 1637195904,
        "sunset": 1637235130
    },
    "timezone": 19800,
    "id": 1271439,
    "name": "Gaya",
    "cod": 200
}



