import tkinter as tk
from tkinter import messagebox


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
    ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', ' ': '/'
}

def show_help():
    help_message = "This program allows you to encrypt a message into Morse code or decrypt Morse code into plain text."
    messagebox.showinfo("Help", help_message)

def start_application():
    splash_screen.destroy()

    def encrypt():
        plaintext = text_entry.get("1.0", tk.END).strip()
        encrypted = ""
        for char in plaintext:
            if char.upper() in morse_code_dict:
                encrypted += morse_code_dict[char.upper()] + " "
        encrypted_text.set(encrypted)

    def decrypt():
        code = code_entry.get("1.0", tk.END).strip()
        decrypted = ""
        letters = code.split(" ")
        for letter in letters:
            for key, value in morse_code_dict.items():
                if letter == value:
                    decrypted += key
                    break
        decrypted_text.set(decrypted)
        
    # Create the main window
    window = tk.Tk()
    window.title("Morse Code Encryption and Decryption")

    # Create labels
    label1 = tk.Label(window, text="Enter message to encrypt:")
    label1.pack()

    # Create text entry
    text_entry = tk.Text(window, height=5, width=50)
    text_entry.pack()

    # Create encrypt button
    encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
    encrypt_button.pack()

    # Create encrypted text label
    encrypted_text = tk.StringVar()
    encrypted_label = tk.Label(window, textvariable=encrypted_text)
    encrypted_label.pack()

    # Create labels
    label2 = tk.Label(window, text="Enter Morse code to decrypt:")
    label2.pack()

    # Create code entry
    code_entry = tk.Text(window, height=5, width=50)
    code_entry.pack()

    # Create decrypt button
    decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
    decrypt_button.pack()

    # Create decrypted text label
    decrypted_text = tk.StringVar()
    decrypted_label = tk.Label(window, textvariable=decrypted_text)
    decrypted_label.pack()

    # Start the main loop
    window.mainloop()


# Create the splash screen
splash_screen = tk.Tk()
splash_screen.title("Morse Code Application")

# Create labels
title_label = tk.Label(splash_screen, text="Morse Code Encryption and Decryption", font=("Arial", 16))
title_label.pack(pady=20)

# Create buttons
start_button = tk.Button(splash_screen, text="Start", width=15, command=start_application)
start_button.pack(pady=10)

help_button = tk.Button(splash_screen, text="Help", width=15, command=show_help)
help_button.pack(pady=10)

quit_button = tk.Button(splash_screen, text="Quit", width=15, command=splash_screen.quit)
quit_button.pack(pady=10)

# Start the splash screen main loop
splash_screen.mainloop()