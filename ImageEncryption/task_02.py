from tkinter import *  # Import Tkinter library for GUI components
from tkinter import filedialog, simpledialog, messagebox  # Import additional Tkinter modules for file dialog, input dialog, and message boxes
import os  # Import os module for file operations

root = Tk()  # Create the main Tkinter window
root.geometry("300x200")  # Set the window size
root.title("Image Encryptor & Decryptor")  # Set the window title


# Function to process image (encryption or decryption based on mode)
def process_image(mode):
    # Open file dialog to choose an image file
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg;*.png;*.jpeg')])
    
    if not file_path:  # If no file is selected, show a warning
        messagebox.showwarning("Warning", "No file selected.")
        return

    # Custom popup to ask user for a numeric key for encryption/decryption
    key = simpledialog.askstring(
        "Enter Key",  # Popup title
        "Enter a custom numeric key (e.g., 123):\n\nNote: The same key must be used for encryption and decryption."
    )
    
    if not key:  # If no key is entered, show an error
        messagebox.showerror("Error", "Key is required to proceed.")
        return

    # Ensure the entered key is a valid integer
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a valid integer.")
        return

    key = int(key)  # Convert the key to an integer

    try:
        with open(file_path, 'rb') as file:  # Open the image file in binary mode
            original_data = bytearray(file.read())  # Read the image data into a bytearray

        # Perform XOR operation for encryption or decryption
        processed_data = bytearray(original_data)  # Make a copy of the original data
        for i in range(len(processed_data)):  # XOR each byte of the image data with the key
            processed_data[i] ^= key

        # If decrypting, check if the decrypted data matches the original (indicating an incorrect key)
        if mode == "decrypt" and processed_data == original_data:
            messagebox.showerror(
                "Decryption Failed",  # Show error if decryption fails
                "Incorrect key entered. Please try again with the correct key."
            )
            return

        # Write the processed (encrypted or decrypted) data back to the file
        with open(file_path, 'wb') as file:
            file.write(processed_data)

        if mode == "decrypt":  # If decrypting, open the file after processing
            os.startfile(file_path)

        # Show a success message after encryption or decryption
        messagebox.showinfo(
            "Success",
            f"Image {mode}ed successfully!\n\nNote: Remember your key for future use."
        )

    except Exception as e:  # Catch any exceptions and show an error message
        messagebox.showerror("Error", f"An error occurred: {e}")


# Function to encrypt the image by calling process_image with "encrypt" mode
def encrypt_image():
    process_image("encrypt")


# Function to decrypt the image by calling process_image with "decrypt" mode
def decrypt_image():
    process_image("decrypt")


# GUI Components
Label(root, text="Click below to Encrypt or Decrypt").place(x=60, y=50)  # Label instructing the user
Label(root, text="Note: Encrypt or Decrypt same key").place(x=60, y=70)  # Note about using the same key for both actions
Button(root, text="Encrypt", command=encrypt_image).place(x=110, y=100)  # Button to trigger image encryption
Button(root, text="Decrypt", command=decrypt_image).place(x=110, y=140)  # Button to trigger image decryption

root.mainloop()  # Start the Tkinter main loop to keep the window open
