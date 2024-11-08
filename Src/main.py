from PassphraseGenerator import passphrase_generator
from Password_EncDec import FileEncryption, FileDecryption

# This will print a message to the console
print("Hello, World!")
print("testing")

passphrase_generator()
FileEncryption("testDoc.txt", "pass", "testDoc.enc")
FileDecryption("testDoc.enc", "pass")