import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

guess = input("Guess a letter: ").lower()

display = []
display += "_" * len(chosen_word)

position = 0

for letter in chosen_word:
    if guess == letter:
        display[position] = letter
    position += 1

print(display)
