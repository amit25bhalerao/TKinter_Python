import customtkinter as ctk
import tkinter.messagebox as messagebox


def add_todo():
    todo = entry.get().strip()
    if not todo:
        messagebox.showinfo("Empty Entry", "Please Enter a Task before Adding.")
        return

    label_frame = ctk.CTkFrame(scrollable_frame)
    label_frame.pack(fill="x")

    label = ctk.CTkLabel(label_frame, text=todo)
    label.pack(side="left")

    erase_button = ctk.CTkButton(label_frame, text="Erase", command=lambda frame=label_frame, lbl=label: erase_entry(frame, lbl))
    erase_button.pack(side="right")

    entry.delete(0, ctk.END)

    # Save the entry to the file
    with open("entries.txt", "a") as file:
        file.write(todo + "\n")


def erase_entry(label_frame, label):
    label_frame.destroy()

    # Remove the erased entry from the file
    with open("entries.txt", "r") as file:
        lines = file.readlines()
    with open("entries.txt", "w") as file:
        for line in lines:
            if line.strip() != label.cget("text"):
                file.write(line)


root = ctk.CTk()
root.geometry("1000x650")
root.title("ToDo App")

title_label = ctk.CTkLabel(root, text="Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=900, height=400)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add ToDo")
entry.pack(fill="x")

addButton = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
addButton.pack(pady=20)

# Load the entries from the file
try:
    with open("entries.txt", "r") as file:
        entries = [line.strip() for line in file]
    for entry_text in entries:
        label_frame = ctk.CTkFrame(scrollable_frame)
        label_frame.pack(fill="x")

        label = ctk.CTkLabel(label_frame, text=entry_text)
        label.pack(side="left")

        erase_button = ctk.CTkButton(label_frame, text="Erase", command=lambda frame=label_frame, lbl=label: erase_entry(frame, lbl))
        erase_button.pack(side="right")
except FileNotFoundError:
    pass

root.mainloop()