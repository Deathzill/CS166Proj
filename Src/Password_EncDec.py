from aes_cipher import FileEncrypter, FileDecrypter, Pbkdf2Sha512Default
import os

def FileEncryption(FileName, password, outputFileName):
    salt = os.urandom(16)
    encrypter = FileEncrypter(Pbkdf2Sha512Default)

    encrypter.Encrypt(FileName, [password], [salt])
    enc_data = encrypter.GetEncryptedData()
    
    with open(outputFileName, 'wb') as file:
        file.write(enc_data)


def FileDecryption(FileName, password):
    decrypter = FileDecrypter(Pbkdf2Sha512Default)

    decrypter.Decrypt(FileName, [password])
    data = decrypter.GetDecryptedData()

    data = data.decode('utf-8')

    print(data)
    return data

FileEncryption("testDoc.txt", "pass", "testDoc.enc")
FileDecryption("testDoc.enc", "pass")