import random
words = ["ravens", "bulldog", "bowie", "miles", "picture", "turkey", "pie"]
secret_word = random.choice(words)
dashes = "*" * len(secret_word)
guesses_left = 10

while dashes != secret_word and guesses_left > 0:
    print(dashes)
    print(f"{guesses_left} incorrect guesses left.")
    guess = input("Guess: ")

    if len(guess) != 1:
        print("Your guess must have exactly one character!")
        continue
    if not guess.islower() or not guess.isalpha():
        print("Your guess must be a lowercase letter!")
        continue

    if guess in secret_word:
        print("That letter is in the word!")
        result = ""
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                result += guess
            else:
                result += dashes[i]
        dashes = result
    else:
        print("That letter is not in the word.")
        guesses_left -= 1

if dashes == secret_word:
    print(f"Congrats! You win 500 million dollars! The word was: {secret_word}")
else:
    print(f"You lose. Better luck next time. The word was: {secret_word}")