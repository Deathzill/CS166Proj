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

    check_num = False
    check_capital = False
    check_special_char = False

    for char in password:
        if include_numbers and char.isdigit():
            check_num = True
        if capitalize and char.isupper():
            check_capital = True

    if include_specialchar:
        check_special_char = any(not char.isalnum() for char in password)

    p = list(password)
    if include_numbers and not check_num:
        p[len(password) - 1] = random.choice(string.digits)
    if include_numbers and not check_capital:
        p[len(password) - 2] = random.choice(string.ascii_uppercase)
    if include_specialchar and not check_special_char:
        p[len(password) - 3] = random.choice(string.punctuation)

    password = "".join(p)

    return password