import tkinter as tk
import re

# Morse Code Dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
}

def start_program():
    home_screen.pack_forget()
    play_screen.pack()

def show_help():
    home_screen.pack_forget()
    help_screen.pack()
    help_text = "  This program encodes and decodes both morse code and text.  \n\n" \
                "  Enter your message in the text box and press the 'decode/encode' button.  \n\n" \
                "  If the message is encoded, the program will decode the typed message.  \n\n" \
                "  Otherwise it will encode the text inputed.  "
    help_label.config(text=help_text, font=("Arial", 13) )

def play_go_back():
    play_screen.pack_forget()
    home_screen.pack()

def help_go_back():
    help_screen.pack_forget()
    home_screen.pack()

def process_message():
    message = input_text.get("1.0", "end-1c")
    if re.match('^[-. /]*$', message):
        # Encoded Morse Code, decode it
        decoded_message = decode_morse(message)
        output_text.delete("1.0", "end")
        output_text.insert("end", decoded_message)
    else:
        # Decoded message, encode it
        encoded_message = encode_morse(message.upper())
        output_text.delete("1.0", "end")
        output_text.insert("end", encoded_message)

def decode_morse(encoded_message):
    decoded_message = ''
    words = encoded_message.strip().split(' / ')
    for word in words:
        letters = word.split()
        for letter in letters:
            for key, value in morse_code.items():
                if value == letter:
                    decoded_message += key
                    break
            else:
                # If no match found, assume it's a space
                decoded_message += ' '
    return decoded_message

def encode_morse(decoded_message):
    encoded_message = ''
    for char in decoded_message:
        if char == ' ':
            encoded_message += '/ '
        elif char.upper() in morse_code:
            encoded_message += morse_code[char.upper()] + ' '
    return encoded_message

# Start app

# Home screen
app = tk.Tk()
app.title("Morse Code Translator")

home_screen = tk.Frame(app)
title_label = tk.Label(app, text="== Morse Code Translator ==", font=("Arial", 26))
title_label.pack(pady=20)

start_button = tk.Button(home_screen, text="Start", width=20, font=("Arial", 20), command=start_program)
start_button.pack(pady=10)

help_button = tk.Button(home_screen, text="Help",width=20, font=("Arial", 18), command=show_help)
help_button.pack(pady=10)

exit_button = tk.Button(home_screen, text="Exit",width=20, font=("Arial", 16), command=app.quit)
exit_button.pack(pady=10)

home_screen.pack()

# Play screen
play_screen = tk.Frame(app)

input_label = tk.Label(play_screen, text="Input:", font=("Arial", 14))
input_label.pack(pady=10)

input_text = tk.Text(play_screen, height=3, width=35, font=("Arial", 15))
input_text.pack()

decode_button = tk.Button(play_screen, text="Decode/Encode", width=15, font=("Arial", 15), command=process_message)
decode_button.pack(pady=10)

output_label = tk.Label(play_screen, text="Output:", font=("Arial", 14))
output_label.pack(pady=10)

output_text = tk.Text(play_screen, height=3, width=35, font=("Arial", 15))
output_text.pack()

back_button = tk.Button(play_screen, text="Back", width=15, font=("Arial", 15), command=play_go_back)
back_button.pack(pady=10)


# Help screen
help_screen = tk.Frame(app)

help_label = tk.Label(help_screen, text="")
help_label.pack(pady=10)

back_button = tk.Button(help_screen, text="Back", width=15, font=("Arial", 15), command=help_go_back)
back_button.pack(pady=10)

# Loop
app.mainloop()
