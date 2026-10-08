import os
import requests
import tkinter as tk

# Silence macOS Tkinter deprecation warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'


def get_weather(event=None):
    city = text_field.get().strip()
    if not city:
        return

    # Visual feedback while fetching
    label1.config(text="Loading...")
    label2.config(text="")
    canvas.update_idletasks()

    # Keyless wttr.in JSON endpoint
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            label1.config(text="Error")
            label2.config(text=f"City '{city}' not found!")
            return

        json_data = response.json()
        
        # Check if wttr.in returned valid weather data
        if 'current_condition' not in json_data:
            label1.config(text="Not Found")
            label2.config(text=f"Could not find weather for '{city}'")
            return

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

    except requests.exceptions.RequestException:
        label1.config(text="Error")
        label2.config(text="Connection Error. Check internet!")
    except Exception:
        label1.config(text="Error")
        label2.config(text="Unable to process weather data")


# Main Window Setup
canvas = tk.Tk()
canvas.geometry("500x550")
canvas.title("Weather App")
canvas.config(bg="#1E1E24")  # Modern dark background

# Fonts
f_small = ("poppins", 13, "normal")
f_medium = ("poppins", 18, "bold")
f_large = ("poppins", 28, "bold")

# Input Field
text_field = tk.Entry(
    canvas,
    justify='center',
    width=18,
    font=f_medium,
    bg="#2D2D3A",
    fg="#FFFFFF",
    insertbackground="#FFFFFF",  # Cursor color
    relief="flat"
)
text_field.pack(pady=(25, 10))
text_field.focus()
text_field.bind('<Return>', get_weather)

# Search Button
search_btn = tk.Button(
    canvas,
    text="Get Weather",
    font=("poppins", 11, "bold"),
    command=get_weather,
    highlightbackground="#1E1E24"
)
search_btn.pack(pady=5)

# Main Temp & Status Label
label1 = tk.Label(canvas, font=f_large, bg="#1E1E24", fg="#00D2FF")
label1.pack(pady=20)

# Detailed Stats Label
label2 = tk.Label(canvas, font=f_small, justify='center', bg="#1E1E24", fg="#E0E0E0")
label2.pack(pady=10)

if __name__ == "__main__":
    canvas.mainloop()