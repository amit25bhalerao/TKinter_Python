import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import pyperclip
import xml.dom.minidom as minidom


def format_xml():
    xml_data = input_text.get("1.0", "end").strip()
    if not xml_data:
        messagebox.showerror("Error", "Please input XML data.")
        return

    try:
        # Parse the XML data
        parsed_xml = minidom.parseString(xml_data)
        # Pretty print the XML with indentation and line breaks
        formatted_xml = parsed_xml.toprettyxml(indent="  ")
        # Remove extra leading whitespace
        formatted_xml = '\n'.join(line for line in formatted_xml.split('\n') if line.strip())
        output_text.config(state="normal")  # Enable the output text area
        output_text.delete("1.0", "end")
        output_text.insert("1.0", formatted_xml)
        output_text.config(state="disabled")  # Disable the output text area
    except Exception as e:
        messagebox.showerror("Error", str(e))


def validate_xml():
    xml_data = input_text.get("1.0", "end").strip()
    if not xml_data:
        messagebox.showerror("Error", "Please input XML data.")
        return

    try:
        # Parse the XML data
        minidom.parseString(xml_data)
        messagebox.showinfo("Success", "Valid XML data.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_text():
    input_text.delete("1.0", "end")
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.config(state="disabled")


def save_file():
    xml_data = output_text.get("1.0", "end").strip()
    if not xml_data:
        messagebox.showwarning("Warning", "No formatted XML data to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML Files", "*.xml")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(xml_data)
        messagebox.showinfo("Success", "Formatted XML data saved successfully.")


def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
    if file_path:
        with open(file_path, "r") as file:
            xml_data = file.read()
        input_text.delete("1.0", "end")
        input_text.insert("1.0", xml_data)


def copy_to_clipboard():
    xml_data = output_text.get("1.0", "end").strip()
    if not xml_data:
        messagebox.showwarning("Warning", "No formatted XML data to copy.")
        return

    pyperclip.copy(xml_data)
    messagebox.showinfo("Success", "Formatted XML data copied to clipboard.")


def search_replace():
    search_term = search_entry.get()
    replace_term = replace_entry.get()
    xml_data = input_text.get("1.0", "end").strip()

    if not xml_data:
        messagebox.showerror("Error", "Please input XML data.")
        return

    if not search_term:
        messagebox.showerror("Error", "Please enter a search term.")
        return

    try:
        # Perform search and replace
        modified_xml = xml_data.replace(search_term, replace_term)

        if modified_xml == xml_data:
            messagebox.showinfo("No Match", "No matching elements found for replacement.")
        else:
            output_text.config(state="normal")  # Enable the output text area
            output_text.delete("1.0", "end")
            output_text.insert("1.0", modified_xml)
            input_text.delete("1.0", "end")
            input_text.insert("1.0", modified_xml)
            output_text.config(state="disabled")  # Disable the output text area
            messagebox.showinfo("Success", "Search and replace completed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
window = tk.Tk()
window.title("XML Formatter")
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
format_button = tk.Button(button_frame, text="Format", command=format_xml)
format_button.pack(side="left", padx=5, pady=5)

# Create the validate button
validate_button = tk.Button(button_frame, text="Validate", command=validate_xml)
validate_button.pack(side="left", padx=5, pady=5)

# Create the clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side="left", padx=5, pady=5)

# Create the save button
save_button = tk.Button(button_frame, text="Save", command=save_file)
save_button.pack(side="left", padx=5, pady=5)

# Create the load button
load_button = tk.Button(button_frame, text="Load", command=load_file)
load_button.pack(side="left", padx=5, pady=5)

# Create the copy button
copy_button = tk.Button(button_frame, text="Copy", command=copy_to_clipboard)
copy_button.pack(side="left", padx=5, pady=5)

# Create the search and replace frame
search_replace_frame = tk.Frame(window)
search_replace_frame.grid(row=1, column=1, sticky="ne", padx=10, pady=10)

# Create the search label and entry
search_label = tk.Label(search_replace_frame, text="Search:")
search_label.pack(side="left", padx=5, pady=5)
search_entry = tk.Entry(search_replace_frame, width=30)
search_entry.pack(side="left", padx=5, pady=5)

# Create the replacement label and entry
replace_label = tk.Label(search_replace_frame, text="Replace:")
replace_label.pack(side="left", padx=5, pady=5)
replace_entry = tk.Entry(search_replace_frame, width=30)
replace_entry.pack(side="left", padx=5, pady=5)

# Create the search and replace button
search_replace_button = tk.Button(search_replace_frame, text="Search and Replace", command=search_replace)
search_replace_button.pack(side="left", padx=5, pady=5)

# Run the main event loop
window.state("zoomed")
window.mainloop()
