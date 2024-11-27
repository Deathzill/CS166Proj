import os
import json
from Password_EncDec.FileEncryption import FileEncryption
from Password_EncDec.FileDecryption import FileDecryption


def initialize_encrypted_file(filename, encrypted_filename, password):
    # Step 1: Encrypt passwords.json if passwords.json.enc does not exist
    if not os.path.exists(encrypted_filename):
        print(f"Encrypting {filename} to create {encrypted_filename}")
        
        # Check if passwords.json exists, create it if necessary
        if not os.path.exists(filename):
            print(f"Creating an empty {filename} file.")
            with open(filename, "w") as f:
                json.dump({}, f)  # Initialize with an empty JSON object

        # Encrypt passwords.json to create passwords.json.enc
        FileEncryption(filename, password, encrypted_filename)
    else:
        print(f"Encrypted file {encrypted_filename} already exists.")

#Loads data from a JSON file.
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Saves data to a JSON file.
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    
# Save a new password or update the existing one. Saves to Json file and re-encrypts it.
def save_password(filename, website, username, password, file_password):
    # Decrypt, load, update, and re-encrypt
    FileDecryption(filename + ".enc", file_password)
    data = load_data(filename)
    
    if website in data:
        print(f"Website '{website}' already exists. Updating password.")
    else:
        print(f"Saving new credentials for website '{website}'.")
        
    data[website] = {"username": username, "password": password}
    save_data(filename, data)
    FileEncryption(filename, file_password, filename + ".enc")


# Retrieves credentials for a specific website by decrypting the JSON file, loading the data, and returning the saved credentials.
def get_password(filename, website, file_password):
    FileDecryption(filename + ".enc", file_password)
    data = load_data(filename)
    return data.get(website, "No credentials found for this website")

def get_all(filename, file_password):
    data = load_data(filename)
    return data

# Delete credentials for a website. Aks for user cnfirmation before deleting.    
def delete_password(filename, website, file_password):
    # Decrypt, load data, and check if website exists
    FileDecryption(filename + ".enc", file_password)
    data = load_data(filename)
    
    if website in data:
        # Ask for confirmation
        confirmation = input(f"Are you sure you want to delete the credentials for '{website}'? (yes/no): ").strip().lower()
        
        if confirmation == 'yes':
            del data[website]
            print(f"Credentials for website '{website}' have been deleted.")
            # Save and re-encrypt
            save_data(filename, data)
            FileEncryption(filename, file_password, filename + ".enc")
        else:
            print("Deletion cancelled.")
    else:
        print(f"No credentials found for website '{website}' to delete.")
    
    save_data(filename, data)
    FileEncryption(filename, file_password, filename + ".enc")
