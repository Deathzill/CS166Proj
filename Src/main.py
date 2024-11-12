import os
import json
from UserInterface import App
from PassphraseGenerator import passphrase_generator
from Password_EncDec.FileEncryption import FileEncryption
from Password_EncDec.FileDecryption import FileDecryption
from Password_Manager import initialize_encrypted_file, save_password, get_password


# This will print a message to the console
print("Hello, World!")
print("testing")

# Define paths
filename = "Src/passwords.json"
encrypted_filename = "Src/passwords.json.enc"

# Password for encryption and decryption
password = "your_password"

# Initialize the encrypted file
initialize_encrypted_file(filename, encrypted_filename, password)


# Uncomment if needed
# FileEncryption("testDoc.txt", "pass", "testDoc.enc")
# FileDecryption("testDoc.enc", "pass")

#****************************** Password Manager Testing Starts ************************

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

#****************************** Password Manager Testing Ends ***************************************

app = App()
app.mainloop()