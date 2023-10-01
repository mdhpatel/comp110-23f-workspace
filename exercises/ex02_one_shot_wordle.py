"""EX02 - one_shot_wordle - The actual wordle."""

__author__ = "730710742"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
emojis: str = ""


secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess? ")
while len(guess_word) != len(secret_word):
    guess_word = input("That was not 6 letters! Try again: ")

while index < len(secret_word):
    if secret_word[index] == guess_word[index]:
        emojis += GREEN_BOX
    else:
        exists: bool = False
        alternate_index: int = 0
        while (exists is not True) and (alternate_index < len(secret_word)):
            if secret_word[alternate_index] == guess_word[index]:
                exists = True
            else:
                alternate_index += 1
        if exists is True:
            emojis += YELLOW_BOX
        elif exists is not True:
            emojis += WHITE_BOX
    index += 1

print(emojis)

if str(guess_word) != str(secret_word) and len(guess_word) == len(secret_word):
    print("Not quite. Play again soon!")
if str(guess_word) == str(secret_word) and len(guess_word) == len(secret_word):
    print("Woo! You got it!")