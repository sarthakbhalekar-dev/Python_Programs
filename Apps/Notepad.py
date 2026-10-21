
import tkinter as tk
from tkinter import filedialog

# Create window
window = tk.Tk()
window.title("My Notepad")
window.geometry("700x500")

# Functions
def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            text.delete("1.0", tk.END)
            text.insert("1.0", f.read())

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(text.get("1.0", "end-1c"))

def clear_text():
    text.delete("1.0", tk.END)

# Buttons
buttons = tk.Frame(window)
buttons.pack(pady=10)

tk.Button(buttons, text="Open", command=open_file, width=10).pack(side="left", padx=5)
tk.Button(buttons, text="Save", command=save_file, width=10).pack(side="left", padx=5)
tk.Button(buttons, text="Clear", command=clear_text, width=10).pack(side="left", padx=5)
tk.Button(buttons, text="Exit", command=window.destroy, width=10).pack(side="left", padx=5)

# Writing area
text = tk.Text(window, font=("Arial", 14), wrap="word")
text.pack(fill="both", expand=True, padx=10, pady=10)

# Start app
window.mainloop()
