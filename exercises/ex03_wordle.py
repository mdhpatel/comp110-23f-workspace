"""EX03 - wordle - The actual wordle with multiple tries."""

__author__ = "730710742"

def contains_char(word: str, character: str)-> bool:
    """returns true or false depending on if character is found within word"""
    assert len(character) == 1
    index: int = 0
    while index < len(word):
        if word[index] == character:
            return True
        index += 1
    return False

def emojified(guess: str, secret: str)-> str:
    """returns a string of emojis based on how the guess string relates to the secret string, using white, yellow, and green blocks"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji_string: str = ""
    while index < len(secret):
        match: bool = contains_char(secret, guess[index])
        if match == True:
            if secret[index] == guess[index]:
                emoji_string += GREEN_BOX
            else:
                emoji_string += YELLOW_BOX
        elif match == False:
            emoji_string += WHITE_BOX
        index += 1
    return emoji_string

def input_guess(expected_length: int)-> str:
    """returns a string of correct length based off the user's input"""
    guess: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(guess) != expected_length:
        guess = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    guess: str = ""
    turns: int = 1
    while turns <= 6 and guess != secret:
        print(f"=== Turn {str(turns)}/6 wo===")
        guess: str = input_guess(len(secret))
        emoji_string: str = emojified(guess, secret)
        print(emoji_string)
        if guess == secret:
            print("You won in " + turns + "/6 turns!")
        elif guess != secret and turns == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turns += 1

if __name__ == "__main__":
    main()