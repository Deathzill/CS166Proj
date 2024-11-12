import os
import json
from UserInterface import App
from PassphraseGenerator import passphrase_generator
from Password_EncDec.FileEncryption import FileEncryption
from Password_EncDec.FileDecryption import FileDecryption
from Password_Manager import save_password, get_password

# This will print a message to the console
print("Hello, World!")
print("testing")

# Uncomment if needed
# FileEncryption("testDoc.txt", "pass", "testDoc.enc")
# FileDecryption("testDoc.enc", "pass")


#****************************** Password Manager Testing

# Password for encryption and decryption
password = "your_password"

#****************************** Password Manager Testing

# Step 1: Encrypt passwords.json if passwords.json.enc does not exist
if not os.path.exists("Src/passwords.json.enc"):
    print("Encrypting passwords.json to create passwords.json.enc")
    
    # Check if passwords.json exists, create it if necessary
    if not os.path.exists("Src/passwords.json"):
        print("Creating an empty passwords.json file.")
        with open("Src/passwords.json", "w") as f:
            json.dump({}, f)  # Initialize with an empty JSON object

    # Encrypt passwords.json to create passwords.json.enc
    FileEncryption("Src/passwords.json", password, "Src/passwords.json.enc")
else:
    print("Encrypted file passwords.json.enc already exists.")

# Example parameters for passphrase_generator
num_words = 4
capitalize = True
include_numbers = True
separator = "-"

# Generate a password with the specified parameters
generated_password = passphrase_generator(num_words, capitalize, include_numbers, separator)
filename = 'Src/passwords.json'
print("Generated Password:", generated_password)

# Step 2: Save new password for a website
# This function handles decryption, updating, and re-encryption. 
# Should be called save_password(filename, website, username, password, file_password):
save_password(filename, 'example.com', 'user123', generated_password, password)

# Step 3: Retrieve and print the password for the website to check if it saved correctly
# Called as def get_password(filename, website, file_password):
credentials = get_password(filename, 'example.com',password)
print("Retrieved credentials:", credentials)

app = App()
app.mainloop()