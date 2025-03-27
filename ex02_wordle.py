"""This is EX02! AKA: the Wordle Assignment for COMP110"""

__author__: str = "730576361"


def contains_char(whole_word: str, single_letter: str) -> bool:
    """Checks if any single letter of the guessed word is in the secret word."""
    assert len(single_letter) == 1, f"len('{single_letter}') is not 1"
    idx: int = 0
    while idx <= len(whole_word) - 1:
        """Tells program to cycle through each letter of guessed word ."""
        if whole_word[idx] == single_letter:
            return True
        else:
            idx += 1
    return False


"""These strings establish the shapes and colors for the boxes in the program."""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(secret_word: str, guessed_word: str) -> str:
    """Colored boxes will appear corresponding to the letters in the secret word."""
    assert len(guessed_word) == len(secret_word), "Guess must be same length as secret"
    colored_boxes: str = ""
    idx: int = 0
    while idx < len(secret_word):
        """Colors each box according to the accuracy of guesed word at each index."""
        if (guessed_word)[idx] == (secret_word)[idx]:
            colored_boxes += GREEN_BOX
        else:
            if contains_char(guessed_word, secret_word[idx]):
                colored_boxes += YELLOW_BOX
            else:
                colored_boxes += WHITE_BOX
        idx += 1
    return colored_boxes


def input_guess(guess_length: int) -> str:
    """Prompts user to guess a word of the same length as the secret word."""
    guessed_word: str = input(f"Enter a {str(guess_length)} character word: ")
    while len(guessed_word) != guess_length:
        """Prevents user from entering a word that is not of the correct length."""
        guessed_word = input(f"That wasn't {str(guess_length)} chars! Try again: ")
    else:
        return guessed_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    print(f"=== Turn {str(turn)}/6 ===")
    turn += 1
    guessed_word: str = input_guess(len(secret_word))
    accurate: bool = True
    while accurate is True and turn <= 6:
        """Based on user input, increases # of turns until game is won or lost."""
        if secret_word == guessed_word or turn > 6:
            accurate = False
        if secret_word != guessed_word:
            print(emojified(guessed_word, secret_word))
            print(f"=== Turn {str(turn)}/6 ===")
            guessed_word = input_guess(len(secret_word))
            turn += 1
        else:
            if secret_word == guessed_word:
                print(emojified(guessed_word, secret_word))
                print(f"You won in {str(turn-1)}/6 turns!")
                accurate = False
        if secret_word != guessed_word and turn > 6:
            print(emojified(guessed_word, secret_word))
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
