import random
import string


def password_generator():
    num_chars_option = input("Enter number of characters (choose from 8-24): ")
    num_chars = int(num_chars_option)
    cap_option = input("Include capital letters? (y/n) ").lower().strip() == 'y'
    capitalize = bool(cap_option)
    num_option = input("Include numbers? (y/n) ").lower().strip() == 'y'
    include_numbers = bool(num_option)
    include_specialchar_option = input ("Include special characters? (y/n) ").lower().strip() == 'y'
    include_specialchar = bool(include_specialchar_option)

    # include_words_option = input ("Include words? (y/n) ").lower().strip() == 'y'
    # include_words = bool(include_words_option)

    password = ""
    characters = string.ascii_lowercase

    if capitalize:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_specialchar:
        characters += string.punctuation

    for i in range(num_chars):
        password = password + random.choice(characters)

    print(password)