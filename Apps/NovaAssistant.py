
import datetime
import random
import subprocess
import sys
import webbrowser
from pathlib import Path
from urllib.parse import quote_plus

import pyttsx3
import speech_recognition as sr


# ---------- SETUP ----------

engine = None

try:
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)
except Exception as error:
    print("Voice output unavailable:", error)

recognizer = sr.Recognizer()
notes_file = Path(__file__).with_name("nova_notes.txt")


# ---------- SPEAK ----------

def speak(message):
    print("Nova:", message)

    if engine is not None:
        try:
            engine.say(message)
            engine.runAndWait()
        except Exception as error:
            print("Speech error:", error)


# ---------- LISTEN ----------

def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(
                source, duration=0.5
            )
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower().strip()

    except sr.WaitTimeoutError:
        print("No speech detected.")

    except sr.UnknownValueError:
        print("Couldn't understand your voice.")

    except sr.RequestError:
        print("Speech recognition needs internet access.")

    except (OSError, AttributeError) as error:
        print("Microphone error:", error)

    return ""


# ---------- INPUT ----------

def get_command(mode):
    if mode == "voice":
        command = listen()

        if command:
            return command

        print("Switching to keyboard for this command.")

    return input("You: ").lower().strip()


# ---------- OPEN WEBSITES ----------

def open_website(name, url):
    webbrowser.open(url)
    speak("Opening " + name)


# ---------- OPEN MAC APPS ----------

def open_app(app_name):
    if sys.platform != "darwin":
        speak("This feature is designed for macOS.")
        return

    apps = {
        "calculator": "Calculator",
        "notes": "Notes",
        "safari": "Safari",
        "calendar": "Calendar",
        "textedit": "TextEdit"
    }

    app = apps.get(app_name)

    if app is None:
        speak("I don't know that app.")
        return

    result = subprocess.run(
        ["open", "-a", app],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        speak("Opening " + app)
    else:
        speak("I couldn't open " + app)


# ---------- SAVE NOTES ----------

def save_note(note):
    if not note:
        speak("There is nothing to save.")
        return

    timestamp = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )

    with open(notes_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {note}\n")

    speak("Your note has been saved.")


# ---------- COMMANDS ----------

def handle_command(command):
    if not command:
        return True

    # Exit
    if command in ["bye", "goodbye", "stop", "exit", "quit"]:
        speak("Goodbye! See you later.")
        return False

    # Greetings
    elif command in ["hello", "hi", "hey", "hello nova"]:
        speak("Hello! How can I help you?")

    elif "how are you" in command:
        speak("I'm doing great! Thanks for asking.")

    # Time and date
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + now)

    elif "date" in command or "what day" in command:
        today = datetime.datetime.now().strftime(
            "%A, %d %B %Y"
        )
        speak("Today is " + today)

    # Websites
    elif "youtube" in command:
        open_website(
            "YouTube",
            "https://www.youtube.com"
        )

    elif "gmail" in command:
        open_website(
            "Gmail",
            "https://mail.google.com"
        )

    elif "wikipedia" in command:
        open_website(
            "Wikipedia",
            "https://www.wikipedia.org"
        )

    elif "google" in command and "search" not in command:
        open_website(
            "Google",
            "https://www.google.com"
        )

    # Weather
    elif "weather" in command:
        city = input("Enter city: ").strip()

        if city:
            url = (
                "https://www.google.com/search?q="
                + quote_plus("weather in " + city)
            )
            open_website("weather for " + city, url)
        else:
            speak("No city was entered.")

    # Web search
    elif command.startswith("search "):
        query = command[7:].strip()

        if query:
            url = (
                "https://www.google.com/search?q="
                + quote_plus(query)
            )
            open_website("search results", url)
        else:
            speak("Please give me something to search.")

    # Mac applications
    elif command.startswith("open "):
        app_name = command[5:].strip()
        open_app(app_name)

    # Notes
    elif command.startswith("note "):
        save_note(command[5:].strip())

    elif command in ["read notes", "show notes"]:
        if notes_file.exists():
            content = notes_file.read_text(
                encoding="utf-8"
            )
            print("\n--- YOUR NOTES ---")
            print(content)
            print("------------------\n")
            speak("I've displayed your notes.")
        else:
            speak("You haven't saved any notes yet.")

    # Fun
    elif "joke" in command:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer get cold? It left its Windows open!",
            "There are 10 types of people. Those who understand binary, and those who don't."
        ]
        speak(random.choice(jokes))

    elif "flip a coin" in command:
        speak(random.choice(["Heads!", "Tails!"]))

    elif "roll a dice" in command:
        speak("You rolled " + str(random.randint(1, 6)))

    # Identity
    elif "who are you" in command:
        speak("I'm Nova, your Python personal assistant.")

    # Help
    elif "help" in command:
        print("""
AVAILABLE COMMANDS

hello
time
date
open youtube
open google
open gmail
open wikipedia
open calculator
open notes
open safari
open calendar
open textedit
weather
search Python tutorials
note finish homework
read notes
tell me a joke
flip a coin
roll a dice
who are you
bye
""")
        speak("Here are my available commands.")

    else:
        speak("I don't know that command yet.")

    return True


# ---------- MAIN PROGRAM ----------

def main():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning! I'm Nova.")
    elif hour < 18:
        speak("Good afternoon! I'm Nova.")
    else:
        speak("Good evening! I'm Nova.")

    print("\nNOVA 2.0")
    print("1. Voice mode")
    print("2. Keyboard mode")

    choice = input("Choose 1 or 2: ").strip()
    mode = "voice" if choice == "1" else "keyboard"

    speak("Nova is ready. Say or type help for commands.")

    while True:
        try:
            command = get_command(mode)

            if not handle_command(command):
                break

        except (KeyboardInterrupt, EOFError):
            print()
            speak("Goodbye!")
            break

        except Exception as error:
            print("Error:", error)
            speak("Something went wrong. Please try again.")


if __name__ == "__main__":
    main()
