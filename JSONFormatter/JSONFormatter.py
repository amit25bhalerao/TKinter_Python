import tkinter as tk
import tkinter.messagebox as messagebox
import json
import tkinter.filedialog as filedialog
import pyperclip


def format_json():
    json_data = input_text.get("1.0", "end").strip()
    if not json_data:
        messagebox.showerror("Error", "Please input JSON data.")
        return

    try:
        formatted_json = json.dumps(json.loads(json_data), indent=4)
        output_text.config(state="normal")  # Enable the output text area
        output_text.delete("1.0", "end")
        output_text.insert("1.0", formatted_json)
        output_text.config(state="disabled")  # Disable the output text area
    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_text():
    input_text.delete("1.0", "end")
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.config(state="disabled")


def save_file():
    json_data = output_text.get("1.0", "end").strip()
    if not json_data:
        messagebox.showwarning("Warning", "No formatted JSON data to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(json_data)
        messagebox.showinfo("Success", "Formatted JSON data saved successfully.")


def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "r") as file:
            json_data = file.read()
        input_text.delete("1.0", "end")
        input_text.insert("1.0", json_data)


def minify_json():
    json_data = input_text.get("1.0", "end").strip()
    if not json_data:
        messagebox.showerror("Error", "Please input JSON data.")
        return

    try:
        minified_json = json.dumps(json.loads(json_data), separators=(",", ":"))
        output_text.config(state="normal")  # Enable the output text area
        output_text.delete("1.0", "end")
        output_text.insert("1.0", minified_json)
        output_text.config(state="disabled")  # Disable the output text area
    except Exception as e:
        messagebox.showerror("Error", str(e))


def validate_json():
    json_data = input_text.get("1.0", "end").strip()
    if not json_data:
        messagebox.showerror("Error", "Please input JSON data.")
        return

    try:
        json.loads(json_data)
        messagebox.showinfo("Success", "Valid JSON data.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def copy_to_clipboard():
    json_data = output_text.get("1.0", "end").strip()
    if not json_data:
        messagebox.showwarning("Warning", "No formatted JSON data to copy.")
        return

    pyperclip.copy(json_data)
    messagebox.showinfo("Success", "Formatted JSON data copied to clipboard.")


# Create the main window
window = tk.Tk()
window.title("JSON Formatter")
window.resizable(False, False)  # Fix the window size

# Create the input text area
input_text = tk.Text(window, height=60, width=117)
input_text.grid(row=0, column=0, padx=10, pady=10)

# Create the output text area
output_text = tk.Text(window, height=60, width=117, state="disabled")
output_text.grid(row=0, column=1, padx=10, pady=10)

# Create the button frame
button_frame = tk.Frame(window)
button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create the format button
format_button = tk.Button(button_frame, text="Format", command=format_json)
format_button.pack(side="left", padx=5, pady=5)

# Create the clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side="left", padx=5, pady=5)

# Create the save button
save_button = tk.Button(button_frame, text="Save", command=save_file)
save_button.pack(side="left", padx=5, pady=5)

# Create the load button
load_button = tk.Button(button_frame, text="Load", command=load_file)
load_button.pack(side="left", padx=5, pady=5)

# Create the minify button
minify_button = tk.Button(button_frame, text="Minify", command=minify_json)
minify_button.pack(side="left", padx=5, pady=5)

# Create the validate button
validate_button = tk.Button(button_frame, text="Validate", command=validate_json)
validate_button.pack(side="left", padx=5, pady=5)

# Create the copy button
copy_button = tk.Button(button_frame, text="Copy", command=copy_to_clipboard)
copy_button.pack(side="left", padx=5, pady=5)

# Run the main event loop
window.state("zoomed")
window.mainloop()
