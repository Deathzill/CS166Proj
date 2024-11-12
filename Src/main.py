from PassphraseGenerator import passphrase_generator
from Password_EncDec import FileEncryption, FileDecryption
from UserInterface import App

def check():
   print("checked")

def generate():
   print("generated")

# This will print a message to the console
print("Hello, World!")
print("testing")

# Uncomment if needed
# FileEncryption("testDoc.txt", "pass", "testDoc.enc")
# FileDecryption("testDoc.enc", "pass")

app = App()
app.mainloop()