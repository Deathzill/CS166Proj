from aes_cipher import FileEncrypter, FileDecrypter, Pbkdf2Sha512Default

def FileDecryption(FileName, password):
    decrypter = FileDecrypter(Pbkdf2Sha512Default)

    decrypter.Decrypt(FileName, [password])
    data = decrypter.GetDecryptedData()

    data = data.decode('utf-8')

    return data