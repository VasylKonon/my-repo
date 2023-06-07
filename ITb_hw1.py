import random

words = ['apple', 'juice', 'banana', 'english', 'telephone', 'kitchen']
rand_word = random.choice(words)
tries = int(input('Enter number of tries: '))
hidden = ['*'] * len(rand_word)
for i in range(tries):
    if '*' not in hidden:
        print('You win!')
        break
    letter = input('Enter your letter: ')
    if len(letter) > 1 and letter != rand_word:
        print("You didn't guess the word.")
    elif len(letter) > 1 and letter == rand_word:
        print('You win!')
        break
    elif letter in rand_word:
        for j in range(len(rand_word)):
            if letter == rand_word[j]:
                hidden[j] = letter
        res = ''.join(hidden)
        print(res)
    elif letter not in rand_word:
        print("You didn't guess the letter.")
else:
    print('Tries are over.')
