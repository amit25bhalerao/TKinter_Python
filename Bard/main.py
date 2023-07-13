import tkinter as tk

import bardapi
import requests
from PIL import Image, ImageTk
import io

token = ''


def clear_content():
    input_text.delete(1.0, tk.END)
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.config(state='disabled')


def submit_content():
    # text = input_text.get(1.0, tk.END)
    # output_text.config(state='normal')
    # output_text.insert(tk.END, text)
    # output_text.config(state='disabled')

    # Get the question from the text area widget.
    question = input_text.get("1.0", "end-1c")

    # Send an API request and get a response.
    response = bardapi.core.Bard(token).get_answer(question)

    # Get the content from the response.
    content = response['content']

    # Display the content in the text area widget.
    output_text.configure(state='normal')
    output_text.insert("end", content + "\n")
    output_text.configure(state='disabled')


# Create the main window
root = tk.Tk()
root.title("Title")

# Maximize the screen
root.state("zoomed")

# Set the background image from a URL
image_url = "https://images.pexels.com/photos/949587/pexels-photo-949587.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750" \
            "&dpr=1"  # Replace with your image URL
response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content))
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))  # Resize image to fit the screen
background_image = ImageTk.PhotoImage(image)

# Create a label to hold the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the input frame
input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, padx=10, pady=80, fill=tk.BOTH, expand=True)

# Create the input title label
input_title_label = tk.Label(input_frame, text="Question")
input_title_label.pack()

# Create the input text box
input_text = tk.Text(input_frame, height=35, width=90)
input_text.pack(pady=2)

# Create the output frame
output_frame = tk.Frame(root)
output_frame.pack(side=tk.LEFT, padx=10, pady=80, fill=tk.BOTH, expand=True)

# Create the output title label
output_title_label = tk.Label(output_frame, text="Solution")
output_title_label.pack()

# Create the output text box
output_text = tk.Text(output_frame, height=35, width=90, state='disabled')
output_text.pack(pady=2)

# Create the submit button.
submit_button = tk.Button(root, text='Submit', highlightbackground='white', highlightthickness=2, width=73, bd=0,
                          command=submit_content)
submit_button.place(x=15, y=675)

# Create the clear button.
clear_button = tk.Button(root, text='Clear', highlightbackground='white', highlightthickness=2, width=73, bd=0,
                         command=clear_content)
clear_button.place(x=783, y=675)

# Configure button colors and font.
submit_button.configure(bg='#4CAF50', fg='white', activebackground='#45A049', activeforeground='white',
                        font=('Arial', 12, 'bold'))
clear_button.configure(bg='#f44336', fg='white', activebackground='#D32F2F', activeforeground='white',
                       font=('Arial', 12, 'bold'))

# Start the main loop
root.mainloop()
