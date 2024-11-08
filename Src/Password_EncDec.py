from aes_cipher import FileEncrypter, FileDecrypter, Pbkdf2Sha512Default

#aes cipher from https://pypi.org/project/aes-cipher/
def FileEncryption(FileName, password, outputFileName):
    encrypter = FileEncrypter(Pbkdf2Sha512Default)

    encrypter.Encrypt(FileName, [password])
    enc_data = encrypter.GetEncryptedData()
    
    with open(outputFileName, 'wb') as file:
        file.write(enc_data)


def FileDecryption(FileName, password):
    decrypter = FileDecrypter(Pbkdf2Sha512Default)

    decrypter.Decrypt(FileName, [password])
    data = decrypter.GetDecryptedData()

    data = data.decode('utf-8')

    return data