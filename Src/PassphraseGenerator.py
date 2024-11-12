import random

# random words generated using WonderWords package: https://pypi.org/project/wonderwords/
from wonderwords import RandomWord

def passphrase_generator(num_words, capitalize, include_numbers, separator):
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
            for word in phrase_words:
                num = random.randint(0, 9)
                phrase_words_numbers.append(word + str(num))
            phrase_words = phrase_words_numbers


        passphrase = separator.join(phrase_words)
        return passphrase