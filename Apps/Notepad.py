import sys
import tkinter as tk
from tkinter import BOTH, END, INSERT, LEFT, WORD, Frame, Text
from tkinter.filedialog import askopenfile, asksaveasfile


def save_file():
    new_file = asksaveasfile(mode="w", filetypes=[("Text Files", "*.txt")])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()


def open_file():
    file = askopenfile(mode="r", filetypes=[("Text Files", "*.txt")])
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)  # Clear current text before loading new file
        entry.insert(INSERT, content)
        file.close()


def clear_file():
    entry.delete(1.0, END)


# Main Window
app = tk.Tk()
app.geometry("450x600")
app.title("Notepad")
app.config(bg="#1E1E24")  # Dark modern background frame

# Top Button Frame
top = Frame(app, bg="#1E1E24")
top.pack(padx=10, pady=8, anchor="nw")

# Action Buttons
b1 = tk.Button(top, text="Open", command=open_file)
b1.pack(side=LEFT, padx=4)

b2 = tk.Button(top, text="Save", command=save_file)
b2.pack(side=LEFT, padx=4)

b3 = tk.Button(top, text="Clear", command=clear_file)
b3.pack(side=LEFT, padx=4)

b4 = tk.Button(top, text="Exit", command=app.destroy)  # Clean window exit
b4.pack(side=LEFT, padx=4)

# Text Editor Area
entry = Text(
    app,
    wrap=WORD,
    bg="#F9DDA4",
    fg="#1E1E24",
    font=("poppins", 15),
    undo=True,  # Enables Cmd+Z undo support!
)
entry.pack(padx=10, pady=(0, 10), expand=True, fill=BOTH)

if __name__ == "__main__":
    app.mainloop()