# Importing Modules
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

# Loading The Voice Assistant
print('Loading Your Personal Voice Assistant, Nova.')

engine = pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', 200)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Code To Wish The User
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning Sir, I'm Your Personal Assistant,Nova Here.")
        print("Hello, Good Morning Sir, I'm Your Personal Assistant,Nova Here.")
    elif hour>=12 and hour<18:
        speak("Hello, Good AfterNoon Sir, I'm Your Personal Assistant,Nova Here.")
        print("Hello, Good AfterNoon Sir, I'm Your Personal Assistant,Nova Here.")
    else:
        speak("Hello, Good Evening Sir, I'm Your Personal Assistant,Nova Here.")
        print("Hello, Good Evening Sir, I'm Your Personal Assistant,Nova Here.")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"User Said: {statement}\n")

        except Exception as e:
            speak("Pardon Me, Can You Speak Again?")
            return "None"
        return statement

speak("Loading Your Personal Voice Assistant, Nova.")
wishMe()

# Main Code
if __name__=='__main__':


    while True:
        speak("How May I Help You Now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Your Voice Assistant, Nova Is Shutting Down, Good Bye!')
            print('Your Voice Assistant, Nova Is Shutting Down, Good Bye!')
            break


# Searching Wikipedia
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("Wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According To Wikipedia..")
            print(results)
            speak(results)

# Opening Applications
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube Is Open Now.")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Is Open Now.")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail Is Open Now.")
            time.sleep(5)

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("StackOverFlow Is Open Now.")

# Predicting Weather
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("What Is The Name Of The City You Live In?")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature In Kelvin Unit Is " +
                      str(current_temperature) +
                      "\n Humidity In Percentage Is " +
                      str(current_humidiy) +
                      "\n Description  " +
                      str(weather_description))
                print(" Temperature In Kelvin Unit = " +
                      str(current_temperature) +
                      "\n Humidity (In Percentage) = " +
                      str(current_humidiy) +
                      "\n Description = " +
                      str(weather_description))

            else:
                speak(" City Not Found. Try Again ! ")


# Predicting Time
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time Is {strTime}")

# Introducing The Voice Assistant
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('My Name Is Nova, Your Personal Voice Assistant. I Am Programmed To Perform Minor Tasks Like'
                  'Opening Youtube,Google,Gmail And StackOverFlow ,Predict Time,Take A photo,Search Wikipedia,Predict Weather' 
                  'In Different Cities , Get Top Headline News From Times Of India And You Can Ask Me Computational Or Geographical Questions Too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I Am Built By RayLight!")
            print("I Am Built By RayLight!")

# Opening News
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here Are Some Headlines From Times Of India ,Happy Reading!')
            time.sleep(6)

# Taking Photos
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

# Searching
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I Can Answer To Computational And Geographical Questions . What Question Do You Want Me To Answer Right Now?')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

# Shutting The Computer Down
        elif "log off" in statement or "sign out" in statement:
            speak("Alright, Your Computer Will Shut Down In 10 Seconds, Make Sure You Exit From All Applications!")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)












