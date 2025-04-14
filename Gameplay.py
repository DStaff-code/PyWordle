import random
from colorama import Fore, Style, init
# Initialize Colorama
init(autoreset=True)

from word_list import Wordlist
from Feedback import Feedback, ColorFeedback

class WordleGameplay:
    def __init__(self, word_filename, max_attempts=6):
        self.wordlist_obj = Wordlist(word_filename)
        self.words = self.wordlist_obj.get_words()
        self.max_attempts = max_attempts

    def print_instructions(self):
        print("Welcome to Wordle!")
        print(f"Guess the five-letter word by typing it into the terminal in {self.max_attempts} attempts.")
        print("The game will then provide feedback for your guess:")
        print("A " + Fore.GREEN + "Green" + Style.RESET_ALL + " letter indicates that the letter is correct and in the correct position.")
        print("A " + Fore.YELLOW + "Yellow" + Style.RESET_ALL + " letter indicates that the letter is correct but in the wrong position.")
        print("A " + Fore.LIGHTBLACK_EX + "Gray" + Style.RESET_ALL + " letter indicates that the letter is incorrect and not in the word.")
        print("Keep guessing until you find the correct word!\n")

    def gameplay(self):
        secret_word = random.choice(self.words)
        attempts = 0
        previous_guesses = set()

        while attempts < self.max_attempts:
            guess = input(f"Enter your guess (attempt {attempts+1}/{self.max_attempts}): ").lower().strip()
            # Avoid duplicate guesses.
            if guess in previous_guesses:
                print("You already guessed that word, try a different word.")
                continue
            previous_guesses.add(guess)

            feedback_obj = Feedback(secret_word, guess)
            
            #Validate guess length and word list membership
            if not feedback_obj.is_valid_length():
                print("Your guess must be exactly 5 letters.")
                continue
            if not feedback_obj.is_valid_word(self.words):
                print("Your guess must be a valid English word from our list.")
                continue

            #Compare guess to secret word and generate feedback.
            feedback = feedback_obj.compare_words()

            #Print color-coded feedback.
            ColorFeedback(feedback).print_feedback()

            attempts += 1

            #Win condition – guess matches secret word.
            if guess == secret_word:
                print("Congratulations! You've guessed the word correctly!")
                break
        else:
            #maximum attempts reached.
            print("Sorry, you've used all attempts. The correct word was:", secret_word.upper())

    def play(self):
        while True:
            self.print_instructions()
            self.gameplay()
            again = input("Do you want to play again? (y/n): ").lower().strip()
            if again == 'n' or again =='no':
                print("Thanks for playing!")
                break
