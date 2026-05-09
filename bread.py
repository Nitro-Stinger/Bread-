import tkinter as tk
from tkinter import ttk
import random

bread_memes = [
    "🍞 Bread 👍",
    "🥖 French bread has entered the chat.",
    "🍞 You have been blessed by the loaf.",
    "🥯 Bagel detected. Threat level: Delicious.",
    "🍞 Loading carbs... 100% complete.",
    "🥐 Croissant moment.",
    "🍞 In bread we trust.",
    "🥖 This is a loafly day.",
    "🍞 Bread jumpscare.",
    "🥯 You can't escape the bread.",
    "🍞 The council of toast approves.",
    "🥐 Warning: Excessive bread consumption.",
    "🍞 Bread.exe is running.",
    "🥖 Garlic bread is peak technology.",
    "🍞 A wild loaf appeared!"
]

root = tk.Tk()
root.title("Bread Meme Compilation")
root.geometry("600x400")
root.configure(bg="wheat")

title = tk.Label(
    root,
    text="🍞 Ultimate Bread Meme Compilation 🍞",
    font=("Arial", 20, "bold"),
    bg="wheat",
    fg="brown"
)
title.pack(pady=20)

meme_label = tk.Label(
    root,
    text=random.choice(bread_memes),
    font=("Comic Sans MS", 18),
    wraplength=500,
    bg="wheat",
    fg="darkred"
)
meme_label.pack(pady=40)

def new_meme():
    meme_label.config(text=random.choice(bread_memes))

def popup_bread():
    popup = tk.Toplevel(root)
    popup.title("BREAD ALERT")
    popup.geometry("300x150")
    popup.configure(bg="bisque")

    popup_label = tk.Label(
        popup,
        text=random.choice(bread_memes),
        font=("Comic Sans MS", 14, "bold"),
        bg="bisque",
        fg="saddlebrown",
        wraplength=250
    )
    popup_label.pack(expand=True)

button_frame = tk.Frame(root, bg="wheat")
button_frame.pack(pady=20)

new_meme_button = ttk.Button(
    button_frame,
    text="New Bread Meme",
    command=new_meme
)
new_meme_button.grid(row=0, column=0, padx=10)

popup_button = ttk.Button(
    button_frame,
    text="Spawn Bread Popup",
    command=popup_bread
)
popup_button.grid(row=0, column=1, padx=10)

def chaos_mode():
    popup_bread()
    delay = random.randint(1000, 4000)
    root.after(delay, chaos_mode)

chaos_button = ttk.Button(
    root,
    text="Activate Bread Chaos",
    command=chaos_mode
)
chaos_button.pack(pady=10)

root.mainloop()