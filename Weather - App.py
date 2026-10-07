import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
import requests

def getWeather(event=None):
    city = textField.get().strip()
    if not city:
        return

    # Use keyless wttr.in JSON endpoint
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            label1.config(text="Error")
            label2.config(text=f"City '{city}' not found!")
            return

        json_data = response.json()
        current = json_data['current_condition'][0]
        weather_desc = current['weatherDesc'][0]['value']
        temp = current['temp_C']
        humidity = current['humidity']
        wind = current['windspeedKmph']
        pressure = current['pressure']

        astronomy = json_data['weather'][0]['astronomy'][0]
        sunrise = astronomy['sunrise']
        sunset = astronomy['sunset']

        final_info = f"{weather_desc}\n{temp}°C"
        final_data = (
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} km/h\n"
            f"Pressure: {pressure} hPa\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}"
        )
        label1.config(text=final_info)
        label2.config(text=final_data)

    except Exception:
        label1.config(text="Error")
        label2.config(text="Connection Error")


canvas = tk.Tk()
canvas.geometry("600x550")
canvas.title("Weather App")

f = ("poppins", 14, "normal")
t = ("poppins", 28, "bold")

textField = tk.Entry(canvas, justify='center', width=18, font=t)
textField.pack(pady=15)
textField.focus()
textField.bind('<Return>', getWeather)

search_btn = tk.Button(canvas, text="Get Weather", font=("poppins", 12, "bold"), command=getWeather)
search_btn.pack(pady=5)

label1 = tk.Label(canvas, font=t)
label1.pack(pady=10)

label2 = tk.Label(canvas, font=f, justify='center')
label2.pack(pady=10)

canvas.mainloop()