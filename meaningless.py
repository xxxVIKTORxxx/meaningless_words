import random
import string

mu = 5.1
sigma = 2.1

letters = []
for letter in string.ascii_lowercase:
    letters.append(letter)

def meaningless_word():
    global letters
    global mu
    global sigma

    word_random_lenght = int(random.gauss(mu, sigma))
    
    random_word = str()
    for letter_random in range(word_random_lenght):
        rand_let = random.choice(letters)
        random_word += rand_let

    return random_word

for n in range(10):
    print(f'{meaningless_word()}')

