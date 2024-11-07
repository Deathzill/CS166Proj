import random

# random words generated using WonderWords package: https://pypi.org/project/wonderwords/
from wonderwords import RandomWord

def passphrase_generator():
        num_words_option = input("Enter number of words (choose from 4 - 10): ")
        num_words = int(num_words_option)
        cap_option = input("Capitalize each word? (y/n) ").lower().strip() == 'y'
        capitalize = bool(cap_option)
        num_option = input("Include numbers? (y/n) ").lower().strip() == 'y'
        include_numbers = bool(num_option)
        separator = input("Enter in the separator (string) to put between each word in the passphrase: ")

        phrase_words = []

        r = RandomWord()
        random_word_list = r.random_words(1000)

        for i in range(0, num_words):
            word = random.SystemRandom().choice(random_word_list)
            phrase_words.append(word)

        if capitalize:
            phrase_words = [phrase_word.capitalize() for phrase_word in phrase_words]

        if include_numbers:
            phrase_words_numbers = []
            for i in range(0, num_words):
                num_list = [random.randrange(1, num_words) for i in range(0,9)]
                for j in num_list:
                    phrase_words_numbers = [word + str(j) for word in phrase_words]
            phrase_words = phrase_words_numbers

        passphrase = separator.join(phrase_words)
        print(passphrase)

