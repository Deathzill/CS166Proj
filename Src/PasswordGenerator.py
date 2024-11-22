import random
import string

def password_generator(num_chars, capitalize, include_numbers, include_specialchar):
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

    return password