import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import datetime

root = tk.Tk()
root.title("Smart Chatbot 🤖")
root.geometry("400x500")
root.configure(bg="#1e1e2f")  # dark background

# Chat area
chat = ScrolledText(
    root,
    bg="#2c2f4a",
    fg="white",
    font=("Arial", 12),
    wrap=tk.WORD
)
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Welcome message
chat.insert(tk.END, "🤖 Bot: Hello! Type something below...\n\n")

# Chatbot logic
def get_response(msg):
    msg = msg.lower()

    if "hi" in msg or "hello" in msg:
        return "Hello! 👋"
    elif "how are you" in msg:
        return "I'm doing great! 😄"
    elif "name" in msg:
        return "I'm your chatbot 🤖"
    elif "who created you" in msg:
        return "Akanksha mishra"
    elif "story" in msg:
        return "what type"
    elif "day" in msg:
        return "its your day! live it enjoy it"
    elif "time" in msg:
        t = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
        return "Time: " + t.strftime("%H:%M:%S")
    elif "date" in msg:
        d = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
        return "Date: " + d.strftime("%d-%m-%Y")
    elif "bye" in msg:
        return "Goodbye! 😊"
    else:
        return "I didn't understand 🤔"

# Send function
def send(event=None):
    msg = entry.get()

    if msg.strip() == "":
        return

    chat.insert(tk.END, "You: " + msg + "\n")
    chat.insert(tk.END, "Bot: " + get_response(msg) + "\n\n")

    entry.delete(0, tk.END)
    chat.yview(tk.END)

# Bottom frame (for input + button)
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(fill=tk.X, padx=10, pady=5)

# Entry box
entry = tk.Entry(
    frame,
    font=("Arial", 12),
    bg="#3b3f5c",
    fg="white",
    insertbackground="white"
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry.bind("<Return>", send)

# Send button
send_btn = tk.Button(
    frame,
    text="Send",
    command=send,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10
)
send_btn.pack(side=tk.RIGHT)

root.mainloop()
