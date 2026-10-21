
import tkinter as tk
from tkinter import ttk
import requests
import threading
from urllib.parse import quote


# Get weather information
def get_weather():
    city = city_entry.get().strip()

    if not city:
        result_label.config(text="Please enter a city!")
        return

    search_button.config(state="disabled")
    result_label.config(text="Loading weather...")
    details_label.config(text="")

    # Run the request without freezing the window
    threading.Thread(
        target=fetch_weather,
        args=(city,),
        daemon=True
    ).start()


def fetch_weather(city):
    try:
        url = f"https://wttr.in/{quote(city, safe='')}?format=j1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        current = data["current_condition"][0]
        astronomy = data["weather"][0]["astronomy"][0]

        description = current["weatherDesc"][0]["value"]
        temperature = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        pressure = current["pressure"]

        sunrise = astronomy["sunrise"]
        sunset = astronomy["sunset"]

        summary = f"{city.title()}\n{temperature}°C\n{description}"

        details = (
            f"Feels Like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind} km/h\n"
            f"Pressure: {pressure} hPa\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}"
        )

        root.after(0, lambda: show_result(summary, details))

    except (requests.RequestException, ValueError, KeyError, IndexError):
        root.after(
            0,
            lambda: show_result(
                "Weather unavailable",
                "Check the city name or internet connection."
            )
        )


def show_result(summary, details):
    result_label.config(text=summary)
    details_label.config(text=details)
    search_button.config(state="normal")


# Main window
root = tk.Tk()
root.title("Weather App")
root.geometry("450x540")
root.configure(bg="#171923")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="☁ Weather App",
    font=("Arial", 24, "bold"),
    bg="#171923",
    fg="white"
)
title_label.pack(pady=(25, 10))

# City input
city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    bg="#292D3E",
    fg="white",
    insertbackground="white",
    relief="flat",
    width=25
)
city_entry.pack(pady=12, ipady=10)
city_entry.focus()

# Search button
search_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 13, "bold"),
    bg="#00B8D9",
    fg="black",
    command=get_weather,
    relief="flat",
    padx=20,
    pady=8
)
search_button.pack(pady=8)

city_entry.bind("<Return>", lambda event: get_weather())

# Weather result
result_label = tk.Label(
    root,
    text="Enter a city to get started",
    font=("Arial", 23, "bold"),
    bg="#171923",
    fg="#59D8F7",
    justify="center"
)
result_label.pack(pady=(25, 12))

# Weather details
details_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#171923",
    fg="#E5E7EB",
    justify="center"
)
details_label.pack(pady=10)

# Footer
footer_label = tk.Label(
    root,
    text="Weather data: wttr.in",
    font=("Arial", 10),
    bg="#171923",
    fg="#9CA3AF"
)
footer_label.pack(side="bottom", pady=15)

root.mainloop()
