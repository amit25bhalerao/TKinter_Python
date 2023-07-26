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
root.title("Bard Tool")

# Resize the window
window_width = 1500
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(False,False)

# Set the background image from a URL
image_url = "https://wallpaperaccess.com/full/5457333.jpg"  # Replace with your image URL
response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content))
image = image.resize((window_width, window_height))  # Resize image to fit the window
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
input_text = tk.Text(input_frame, height=35, width=85)  # Adjust the dimensions to fit the window
input_text.pack(pady=2)

# Create the output frame
output_frame = tk.Frame(root)
output_frame.pack(side=tk.LEFT, padx=10, pady=80, fill=tk.BOTH, expand=True)

# Create the output title label
output_title_label = tk.Label(output_frame, text="Solution")
output_title_label.pack()

# Create the output text box
output_text = tk.Text(output_frame, height=35, width=85, state='disabled')  # Adjust the dimensions to fit the window
output_text.pack(pady=2)

# Create the submit button.
submit_button = tk.Button(root, text='Submit', highlightbackground='white', highlightthickness=2, width=71, bd=0,
                          command=submit_content)
submit_button.place(x=15, y=677.5)  # Adjust the position to fit the window

# Create the clear button.
clear_button = tk.Button(root, text='Clear', highlightbackground='white', highlightthickness=2, width=71, bd=0,
                         command=clear_content)
clear_button.place(x=767, y=677.5)  # Adjust the position to fit the window

# Configure button colors and font.
submit_button.configure(bg='#4CAF50', fg='white', activebackground='#45A049', activeforeground='white',
                        font=('Arial', 12, 'bold'))
clear_button.configure(bg='#f44336', fg='white', activebackground='#D32F2F', activeforeground='white',
                       font=('Arial', 12, 'bold'))

# Start the main loop
root.mainloop()
