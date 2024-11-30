import os
import json
from UserInterface import App
from PassphraseGenerator import passphrase_generator
from Password_EncDec.FileEncryption import FileEncryption
from Password_EncDec.FileDecryption import FileDecryption
from Password_Manager import initialize_encrypted_file, save_password, get_password, delete_password


# This will print a message to the console
print("Welcome to the Password Manager!")
print()

# Define paths
filename = "Src/passwords.json.enc"

# Password for encryption and decryption
password = "your_password"

# Initialize the encrypted file
print("Checking for Initialized file")
initialize_encrypted_file(filename, password)
print()


#****************************** Password Manager Testing Starts ************************

# Example parameters for passphrase_generator
num_words = 4
capitalize = True
include_numbers = True
separator = "-"

# Generate a password with the specified parameters
generated_password = passphrase_generator(num_words, capitalize, include_numbers, separator)
print("Password has been generated")
print("Generated Password:", generated_password)
print()


# Save the password
save_password(filename, 'example.com', 'user123', generated_password, password)
print("Password has been saved.")
print()

save_password(filename, 'Canvas', 'user123', generated_password, password)
print("Password has been saved to file and encrypted")
print()

save_password(filename, 'Instagram', 'user123', generated_password, password)
print("Password has been saved to file and encrypted")
print()

# Retrieve and print the password for the website to check if it saved correctly
# Called as def get_password(filename, website, file_password):
credentials = get_password(filename, 'Instagram',password)
print("File has been decrypted and read.")
print("Retrieved credentials:", credentials)
print()


# Test deleting a password
print("Deleting Entry")
delete_password(filename, 'example.com', password)


# Try retrieving again to confirm deletion
credentials = get_password(filename, 'Instagram', password)
print("Retrieved credentials after deletion:", credentials)

#****************************** Password Manager Testing Ends ***************************************

app = App()
app.mainloop()