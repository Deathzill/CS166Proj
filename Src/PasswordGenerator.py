import random
import re
import string

def password_generator(num_chars, capitalize, include_numbers, include_specialchar):
    password = ""
    characters = string.ascii_lowercase
    special_char = string.punctuation
    special_char += "!@#$%^&*(),.?:{}|<>"

    if capitalize:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_specialchar:
        characters += special_char

    for i in range(num_chars):
        password = password + random.choice(characters)

    check_num = False
    check_capital = False
    check_special_char = False

    if include_numbers:
        check_num = re.search(r'[0-9]', password)
    if capitalize:
        check_capital = re.search(r'[A-Z]', password)

    if include_specialchar:
        check_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    p = list(password)
    if include_numbers and not check_num:
        p[len(password) - 1] = random.choice(string.digits)
    if include_numbers and not check_capital:
        p[len(password) - 2] = random.choice(string.ascii_uppercase)
    if include_specialchar and not check_special_char:
        p[len(password) - 3] = random.choice(special_char)

    password = "".join(p)
    return password