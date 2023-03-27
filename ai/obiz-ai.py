import openai
import tkinter as tk
import os
import random
import keyboard
import time

# Function to create the chat history label, scrollbar, and text box
def create_chat_history_widgets(window):
    # Create a label for the chat history
    chat_history_label = tk.Label(
        window,
        text="Chat History",
        font=("Helvetica", 16, "bold"),
        bg="#36393F",
        fg="#DCDDDE"
    )
    chat_history_label.pack()

    # Create a scrollbar for the chat history
    chat_history_scrollbar = tk.Scrollbar(window)
    chat_history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a text box for the chat history
    chat_history_text = tk.Text(
        window,
        height=20,
        bg="#36393F",
        fg="#DCDDDE",
        font=("Helvetica", 12),
        state="disabled",
        yscrollcommand=chat_history_scrollbar.set
    )
    chat_history_text.pack(pady=10)

    return chat_history_text, chat_history_scrollbar

# Create the main window
root = tk.Tk()
root.title("obiz.ai")

# Create the chat history widgets
chat_history_text, chat_history_scrollbar = create_chat_history_widgets(root)

# Set the chat history scrollbar to scroll the text box
chat_history_scrollbar.config(command=chat_history_text.yview)

# Create a label for the chat input
chat_input_label = tk.Label(root,
                            text="Chat Input",
                            font=("Helvetica", 16, "bold"),
                            bg="#40444B",
                            fg="#DCDDDE")
chat_input_label.pack()

# Create a scrollbar for the chat input
chat_input_scrollbar = tk.Scrollbar(root)
chat_input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text box for the chat input
chat_input_text = tk.Text(root,
                          height=3,
                          bg="#40444B",
                          fg="#DCDDDE",
                          font=("Helvetica", 12),
                          yscrollcommand=chat_input_scrollbar.set)
chat_input_text.pack(pady=10)

# Set the chat input scrollbar to scroll the text box
chat_input_scrollbar.config(command=chat_input_text.yview)


# Create a function to clear the chat history
def clear_chat_history():
    chat_history_text.configure(state="normal")
    chat_history_text.delete("1.0", "end")
    chat_history_text.configure(state="disabled")
    # Add an animation to clear the chat history
    for i in range(10):
        chat_history_text.configure(bg="#36393F" if i % 2 == 0 else "#40444B")
        chat_history_text.update()
        chat_history_text.after(50)

  # Bind the Enter key to the send_chat_message function
root.bind('<Return>', lambda event: send_chat_message())

def send_chat_message():
    message = chat_input_text.get("1.0", "end-1c")
    chat_history_text.configure(state="normal", fg="#003399")
    chat_history_text.insert("end", "You: " + message + "\n", "right_align")
    chat_history_text.configure(state="disabled")
    chat_input_text.delete("1.0", "end")



     # Code to send the message to the chat system goes here

keyboard.add_hotkey('enter', send_chat_message)

   # Create a function to respond to user
def response():
    with open('speech_words.txt', 'r') as f:
        words = f.read().splitlines()
    sentence = ''
    for i in range(random.randint(5, 10)):
        sentence += random.choice(words) + ' '
    return sentence.capitalize().strip()


# Create a function to handle sending a chat message
def send_chat_message():
    message = chat_input_text.get("1.0", "end-1c")
    if message == "":
        alert = tk.Tk()
        alert.title("Error")
        alert_label = tk.Label(alert, text="ERROR: NO INPUT")
        alert_label.pack(padx=10, pady=10)
    else:
        chat_input_text.delete("1.0", "end")
        chat_history_text.configure(state="normal", fg="#6F576F")
        chat_history_text.insert("end", "You: \n" + message + "\n\n", "right_align")
        chat_history_text.configure(state="disabled")

        # Create a loading animation
        chat_history_text.configure(state="normal", fg="#799A80")
        chat_history_text.insert("end", "Obiz: ", "left_align")
        for i in range(3):
            chat_history_text.insert("end", ".")
            root.update()
            time.sleep(0.3)
        # Call the response function and store the result
        response_text = response()

        # Print the response
        chat_history_text.configure(state="normal", fg="#799A80")
        chat_history_text.insert("end", "\b\b\b\n" + "Obiz: \n" + response_text + "\n\n", "left_align")
        chat_history_text.configure(state="disabled")
        
# Create a button to clear the chat history
clear_button = tk.Button(root,
                         text="Clear",
                         command=clear_chat_history,
                         bg="#4CAF50",
                         fg="#000000",
                         font=("Helvetica", 12),
                         padx=10)
clear_button.pack(pady=10)

# Create a button to send a chat message
send_button = tk.Button(root,
                        text="Send",
                        command=send_chat_message,
                        bg="#008CBA",
                        fg="#000000",
                        font=("Helvetica", 12),
                        padx=10)
send_button.pack(pady=10)

# Start the main loop
root.mainloop()