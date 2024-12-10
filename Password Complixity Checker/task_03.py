import tkinter as tk
from tkinter import messagebox, simpledialog
import re
import secrets
import string

# Password rules dictionary defining required criteria for a strong password
PASSWORD_RULES = {
    "min_length": 8,  # Minimum length of the password
    "uppercase": True,  # Password must contain at least one uppercase letter
    "lowercase": True,  # Password must contain at least one lowercase letter
    "numbers": True,  # Password must contain at least one number
    "special_chars": True  # Password must contain at least one special character
}

# Predefined list to categorize the password strength
STRENGTH_METER = ["Weak", "Moderate", "Strong", "Very Strong"]

def calculate_strength(password):
    """Calculate password strength based on the defined rules."""
    strength = 0  # Start with a strength of 0
    feedback = []  # List to store feedback for the user
    
    # Check if password length meets the minimum length requirement
    if len(password) >= PASSWORD_RULES["min_length"]:
        strength += 1
    else:
        feedback.append(f"Use at least {PASSWORD_RULES['min_length']} characters.")
    
    # Check if password contains an uppercase letter
    if PASSWORD_RULES["uppercase"] and any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("Include uppercase letters.")
    
    # Check if password contains a lowercase letter
    if PASSWORD_RULES["lowercase"] and any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("Include lowercase letters.")
    
    # Check if password contains a number
    if PASSWORD_RULES["numbers"] and any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("Include numbers.")
    
    # Check if password contains any special characters
    if PASSWORD_RULES["special_chars"] and any(c in string.punctuation for c in password):
        strength += 1
    else:
        feedback.append("Include special characters.")
    
    # Assign strength category based on the number of rules the password meets
    strength_metric = STRENGTH_METER[min(strength, len(STRENGTH_METER)-1)]
    
    # Return the strength metric and feedback for the user
    return {"strength_metric": strength_metric, "feedback": feedback}


def generate_password():
    """Generate a strong random password."""
    characters = string.ascii_letters + string.digits + string.punctuation  # Allowed characters
    # Generate a random 12-character password
    return ''.join(secrets.choice(characters) for _ in range(12))


def create_passphrase():
    """Generate a random passphrase from predefined words."""
    words = ["blue", "taco", "forest", "light", "moon", "ocean", "star", "rain", "cloud"]
    # Join 4 random words with a hyphen to form a passphrase
    return '-'.join(secrets.choice(words) for _ in range(4))


def check_password_strength():
    """Popup function to check the strength of a password entered by the user."""
    # Ask the user for their password
    password = simpledialog.askstring("Password Strength", "Enter your password:")
    if password:  # If the user has entered a password
        # Calculate the strength of the entered password
        result = calculate_strength(password)
        feedback = "\n".join(result['feedback'])  # Join all feedback into a string
        # Show the strength and feedback to the user
        messagebox.showinfo("Password Strength", f"Strength: {result['strength_metric']}\n\nFeedback:\n{feedback}")


def suggest_password():
    """Popup function to suggest a random strong password."""
    # Generate a random password
    password = generate_password()
    # Show the suggested password to the user
    messagebox.showinfo("Password Suggestion", f"Suggested Password:\n{password}")


def strength_metric_demo():
    """Popup function to show the password strength metric."""
    # Ask the user for their password to check strength
    password = simpledialog.askstring("Strength Metric", "Enter your password:")
    if password:  # If the user enters a password
        # Calculate the strength of the entered password
        result = calculate_strength(password)
        # Show the strength metric to the user
        messagebox.showinfo("Strength Metric", f"Password Strength Metric: {result['strength_metric']}")


def passphrase_mode():
    """Popup function to generate and show a passphrase."""
    # Generate a random passphrase
    passphrase = create_passphrase()
    # Show the generated passphrase to the user
    messagebox.showinfo("Passphrase Mode", f"Generated Passphrase:\n{passphrase}")


# Main GUI function
def main():
    root = tk.Tk()  # Create the main window
    root.title("Password Complexity Checker")  # Set the window title
    root.geometry("400x400")  # Set the window size
    
    # Label at the top of the window
    tk.Label(root, text="Password Complexity Checker", font=("Arial", 16, "bold")).pack(pady=10)
    
    # Button to check the password strength
    tk.Button(root, text="Check Password Strength", command=check_password_strength, width=25).pack(pady=5)
    
    # Button to show the strength metric
    tk.Button(root, text="Strength Metric", command=strength_metric_demo, width=25).pack(pady=5)
    
    # Button to suggest a strong password
    tk.Button(root, text="Suggest Password", command=suggest_password, width=25).pack(pady=5)
    
    # Button to generate and show a passphrase
    tk.Button(root, text="Passphrase Mode", command=passphrase_mode, width=25).pack(pady=5)
    
    # Button to close the application
    tk.Button(root, text="Exit", command=root.destroy, width=25).pack(pady=20)
    
    root.mainloop()  # Run the Tkinter event loop to keep the window open


# Run the application
if __name__ == "__main__":
    main()
