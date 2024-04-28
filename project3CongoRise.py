import random

# List of words for the game
word_list = ["python", "hangman", "programming", "computer", "game", "code"]

def select_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    play_again = True
    while play_again:
        word = select_random_word(word_list)
        guessed_letters = []
        attempts = 6  # Number of attempts before losing
        hangman_figure = [
            "  ____\n |    |\n |    \n |    \n |\n_|___",
            "  ____\n |    |\n |    O\n |    \n |\n_|___",
            "  ____\n |    |\n |    O\n |    |\n |\n_|___",
            "  ____\n |    |\n |    O\n |   /|\ \n |\n_|___",
            "  ____\n |    |\n |    O\n |   /|\ \n |   / \ \n_|___",
            "  ____\n |    |\n |    O\n |   /|\ \n |   / \ \n_|___\nGame Over!"
        ]

        print("Welcome to Hangman!")
        print(display_word(word, guessed_letters))

        while attempts > 0:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                attempts -= 1
                print(hangman_figure[6 - attempts])
                print(f"Incorrect! Attempts left: {attempts}")
            else:
                print("Correct guess!")

            word_display = display_word(word, guessed_letters)
            print(word_display)

            if "_" not in word_display:
                print("Congratulations! You won!")
                break

        if attempts == 0:
            print(f"Game over! The word was '{word}'.")

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != "yes":
            play_again = False

    print("Thanks for playing Hangman!")

if __name__ == "__main__":
    main()
