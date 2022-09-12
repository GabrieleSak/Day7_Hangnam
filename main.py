import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
display += "_" * len(chosen_word)

while "_" in display:
    guess = input("Guess a letter: ").lower()

    position = 0
    for letter in chosen_word:
        if guess == letter:
            display[position] = letter
        position += 1

    print(display)
print("You win")
