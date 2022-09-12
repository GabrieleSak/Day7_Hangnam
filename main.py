import random
import hangman_art
import hangman_words
print(hangman_art.logo)



lives = 6

chosen_word = random.choice(hangman_words.word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
display += "_" * len(chosen_word)
guessed_letters = []

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        guessed_letters += guess
        if guess in chosen_word:
            position = 0
            for letter in chosen_word:
                if guess == letter:
                    display[position] = letter
                position += 1
        else:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])
if lives == 0:
    print("You lose")
else:
    print("You win")
