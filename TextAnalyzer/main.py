import tkinter as tk
from tkinter import messagebox
import re


def count_characters():
    input_text = input_text_area.get("1.0", tk.END)
    character_count = len(input_text) - 1
    messagebox.showinfo("Character Count", f"Total Characters: {character_count}")


def count_words():
    input_text = input_text_area.get("1.0", tk.END)
    words = re.findall(r'\w+', input_text)
    word_count = len(words)
    messagebox.showinfo("Word Count", f"Total Words: {word_count}")


def count_spaces():
    input_text = input_text_area.get("1.0", tk.END)
    space_count = input_text.count(" ")
    messagebox.showinfo("Space Count", f"Total Spaces: {space_count}")


window = tk.Tk()
window.title("Text Analyzer - Ness Digital Engineering (India) Pvt. Ltd.")
window.state("zoomed")

input_text_area = tk.Text(window, height=15)
input_text_area.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

character_count_button = tk.Button(button_frame, text="Character Count", command=count_characters)
character_count_button.pack(side=tk.LEFT, padx=10)

word_count_button = tk.Button(button_frame, text="Word Count", command=count_words)
word_count_button.pack(side=tk.LEFT, padx=10)

space_count_button = tk.Button(button_frame, text="Space Count", command=count_spaces)
space_count_button.pack(side=tk.LEFT, padx=10)

window.mainloop()