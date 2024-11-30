import os
import json
from Password_EncDec.FileEncryption import FileEncryption
from Password_EncDec.FileDecryption import FileDecryption

# Initialize the encrypted file if it doesn't already exist
def initialize_encrypted_file(encrypted_filename, password):
    if not os.path.exists(encrypted_filename):
        print(f"Creating an empty encrypted file: {encrypted_filename}")
        empty_data = json.dumps({})  # Empty JSON object as a string
        FileEncryption(data=empty_data, password=password, output_file=encrypted_filename)
    else:
        print(f"Encrypted file {encrypted_filename} already exists.")

# Save or update a password directly to the encrypted file
def save_password(encrypted_filename, website, username, password, file_password):
    """
    Save or update a password in the encrypted file.
    """
    # Decrypt the existing data
    decrypted_data = json.loads(FileDecryption(encrypted_filename, file_password))

    # Add or update credentials
    if website in decrypted_data:
        print(f"Updating credentials for '{website}'.")
    else:
        print(f"Adding new credentials for '{website}'.")
    decrypted_data[website] = {"username": username, "password": password}

    # Encrypt the updated data
    updated_data = json.dumps(decrypted_data)  # Convert dictionary back to JSON
    FileEncryption(updated_data, file_password, encrypted_filename, is_raw_data=True)
    print("Password saved successfully.")


# Retrieve credentials for a specific website
def get_password(encrypted_filename, website, file_password):
    decrypted_data = json.loads(FileDecryption(encrypted_filename, file_password))
    return decrypted_data.get(website, "No credentials found for this website")

# Retrieve all saved credentials
def get_all(encrypted_filename, file_password):
    decrypted_data = json.loads(FileDecryption(encrypted_filename, file_password))
    return decrypted_data

# Delete credentials for a specific website
def delete_password(encrypted_filename, website, file_password):
    """
    Delete credentials for a specific website from the encrypted file.
    """
    # Decrypt the existing data
    decrypted_data = json.loads(FileDecryption(encrypted_filename, file_password))

    # Check if the website exists in the data
    if website in decrypted_data:
        del decrypted_data[website]  # Remove the entry
        print(f"Deleted credentials for '{website}'.")
    else:
        print(f"No credentials found for '{website}' to delete.")

    # Encrypt the updated data back into the .enc file
    updated_data = json.dumps(decrypted_data)  # Convert the updated dictionary back to JSON
    FileEncryption(updated_data, file_password, encrypted_filename, is_raw_data=True)
    print("Updated encrypted file after deletion.")
