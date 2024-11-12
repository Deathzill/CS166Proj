import json
from Password_EncDec.FileEncryption import FileEncryption
from Password_EncDec.FileDecryption import FileDecryption


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


# Adds new credentials (username and password) for a specific website and saves it in the JSON file, then re-encrypts the file.
def save_password(filename, website, username, password, file_password):
    FileDecryption(filename + ".enc", file_password)
    data = load_data(filename)
    data[website] = {"username": username, "password": password}
    save_data(filename, data)
    FileEncryption(filename, file_password, filename + ".enc")


# Retrieves credentials for a specific website by decrypting the JSON file, loading the data, and returning the saved credentials.
def get_password(filename, website, file_password):
    FileDecryption(filename + ".enc", file_password)
    data = load_data(filename)
    return data.get(website, "No credentials found for this website")

