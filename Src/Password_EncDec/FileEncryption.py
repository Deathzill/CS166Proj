#aes cipher from https://pypi.org/project/aes-cipher/
import os
from aes_cipher import FileEncrypter, Pbkdf2Sha512Default, DataEncrypter

def FileEncryption(input_data, password, output_file_name, is_raw_data=False):
    """
    Encrypts input data (file path or raw string) and writes it to an output file.
    
    Args:
        input_data (str): File path or raw string data to encrypt.
        password (str): Password to use for encryption.
        output_file_name (str): The name of the output encrypted file.
        is_raw_data (bool): Whether `input_data` is raw data. Defaults to False.
    """
    if is_raw_data:
        # Encrypt raw string data
        encrypter = DataEncrypter(Pbkdf2Sha512Default)
        encrypter.Encrypt(input_data, [password])  # Encrypt the string
        encrypted_data = encrypter.GetEncryptedData()  # Get encrypted bytes
    else:
        # Encrypt file contents
        encrypter = FileEncrypter(Pbkdf2Sha512Default)
        encrypter.Encrypt(input_data, [password])  # Encrypt the file
        encrypted_data = encrypter.GetEncryptedData()  # Get encrypted bytes
        os.remove(input_data)  # Remove plaintext file to avoid leaving unencrypted data

    # Write encrypted data to the output file
    with open(output_file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"Encryption complete. Data written to {output_file_name}")
