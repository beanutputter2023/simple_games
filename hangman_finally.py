print("="*20)
print("Welcome to Hangman!")
print("Guess the word")
print("="*20)
import random
from hangman_ref import word
word = random.choice(word)
allowed_errors = 7
guesses = []
done = False
while not done:
    for letter in word:
        if letter.upper() in guesses:
            print(letter.upper(), end="")
        else:
            print("_", end="")
    print("")
    
    guess = input(f"Allowed errors left: {allowed_errors}. Guess a letter:")
    guesses.append(guess.upper())
    if guess.upper() not in word.upper():
        print("Missed guess:", guess.upper())
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.upper() not in guesses:
            done = False

if done:
    print(f"You found the word! It was {word.upper()}")
else:
    print(f"Game Over! The word was {word.upper()}")




