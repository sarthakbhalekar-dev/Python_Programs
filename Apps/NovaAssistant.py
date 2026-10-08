import datetime
import json
import os
import subprocess
import sys
import time
import warnings
import webbrowser

# Mute urllib3 LibreSSL warnings on macOS
warnings.filterwarnings("ignore")

import requests
import speech_recognition as sr
import wikipedia
import wolframalpha

# Optional module for camera capture
try:
    from ecapture import ecapture as ec
except ImportError:
    ec = None

# Loading Voice Engine safely
print("Loading Your Personal Voice Assistant, Nova...")

try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 190)
    voices = engine.getProperty("voices")
    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)
    elif len(voices) > 0:
        engine.setProperty("voice", voices[0].id)
except Exception as e:
    print(f"Warning: TTS Engine init issue: {e}")
    engine = None


def speak(text):
    print(f"Nova: {text}")
    if engine:
        engine.say(text)
        engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello, Good Morning! I'm your personal assistant, Nova.")
    elif 12 <= hour < 18:
        speak("Hello, Good Afternoon! I'm your personal assistant, Nova.")
    else:
        speak("Hello, Good Evening! I'm your personal assistant, Nova.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language="en-in")
            print(f"User Said: {statement}\n")
        except Exception:
            speak("Pardon me, could you please speak again?")
            return "none"
        return statement.lower()


# Main Execution Loop
if __name__ == "__main__":
    wishMe()

    while True:
        speak("How may I help you now?")
        statement = takeCommand()

        if statement == "none":
            continue

        # Exit / Shutdown Voice Loop
        if any(w in statement for w in ["good bye", "ok bye", "stop", "exit", "quit"]):
            speak("Your voice assistant Nova is shutting down. Good bye!")
            break

        # Casual Conversations & Greetings
        elif any(w in statement for w in ["hello", "hi", "hey"]):
            speak("Hello! How can I assist you today?")

        elif "how are you" in statement:
            speak("I'm doing great, thank you for asking! How are you doing?")

        # Wikipedia Search
        elif "wikipedia" in statement:
            speak("Searching Wikipedia...")
            query = statement.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find relevant information on Wikipedia.")

        # Quick Browser Launcher
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now.")

        elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now.")

        elif "open gmail" in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Gmail is open now.")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Stack Overflow is open now.")

        # Weather Forecast (Metric Units)
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            speak("What is the name of the city?")
            city_name = takeCommand()
            
            if city_name != "none":
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
                try:
                    res = requests.get(url).json()
                    if res.get("cod") != "404":
                        temp = res["main"]["temp"]
                        humidity = res["main"]["humidity"]
                        desc = res["weather"][0]["description"]
                        speak(f"The temperature in {city_name} is {temp} degrees Celsius with {desc} and {humidity} percent humidity.")
                    else:
                        speak("City not found. Please try again.")
                except Exception:
                    speak("Unable to retrieve weather data right now.")

        # Current Time
        elif "time" in statement:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")

        # Identity Checks
        elif "who are you" in statement or "what can you do" in statement:
            speak("My name is Nova. I am your assistant built in Python to open apps, check weather, tell time, and search the web.")

        elif "who made you" in statement or "who created you" in statement:
            speak("I was built by RayLight!")

        # News Search
        elif "news" in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are the latest headlines from Times of India.")

        # Camera Integration
        elif "camera" in statement or "take a photo" in statement:
            if ec:
                ec.capture(0, "Nova Camera", "img.jpg")
                speak("Photo captured successfully.")
            else:
                speak("Camera module ecapture is not configured on this machine.")

        # General Google Search
        elif "search" in statement:
            query = statement.replace("search", "").strip()
            webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
            speak(f"Searching Google for {query}")

        # WolframAlpha Computational Questions
        elif "ask" in statement:
            speak("What question would you like to ask?")
            question = takeCommand()
            if question != "none":
                try:
                    client = wolframalpha.Client("R2K75H-7ELALHR35X")
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                except Exception:
                    speak("Sorry, I couldn't get an answer for that query.")

        # Log off / macOS Logout
        elif "log off" in statement or "sign out" in statement:
            speak("Signing out now.")
            if sys.platform == "darwin":
                subprocess.call(["osascript", "-e", 'tell app "System Events" to log out'])
            else:
                subprocess.call(["shutdown", "/l"])