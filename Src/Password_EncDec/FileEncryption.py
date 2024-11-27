import os
from aes_cipher import FileEncrypter, Pbkdf2Sha512Default, DataEncrypter

#aes cipher from https://pypi.org/project/aes-cipher/
def FileEncryption(FileName, password, outputFileName):
    encrypter = FileEncrypter(Pbkdf2Sha512Default)

    encrypter.Encrypt(FileName, [password])
    enc_data = encrypter.GetEncryptedData()
    
    with open(outputFileName, 'wb') as file:
        file.write(enc_data)

    os.remove(FileName)

def FileEncryptionWithJustData(Data, password, outputFileName):
    encrypter = DataEncrypter(Pbkdf2Sha512Default)

    encrypter.Encrypt(Data, [password])
    enc_data = encrypter.GetEncryptedData()
    
    with open(outputFileName, 'wb') as file:
        file.write(enc_data)