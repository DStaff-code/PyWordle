import random
from colorama import Fore, Style, init
#Initialize Colorama
init(autoreset=True)

#Imported classes
from word_list import Wordlist
from Feedback import Feedback, ColorFeedback

class WordleGameplay:
    def __init__(self, word_filename, max_attempts=6):
        self.wordlist_obj = Wordlist(word_filename)
        self.words = self.wordlist_obj.get_words()
        self.max_attempts = max_attempts

    def print_instructions(self):
        #Game start screen and game instructions
        print(f'                  _____    __          __           _ _      ')
        print(f'                 |  __ \   \ \        / /          | | |     ')
        print(f'                 | |__) |   \ \  /\  / /__  _ __ __| | | ___ ')
        print(f'                 |  ___/ | | \ \/  \/ / _ \| \'__/ _` | |/ _ \ ')
        print(f'                 | |   | |_| |\  /\  / (_) | | | (_| | |  __/')
        print(f'                 |_|    \__, | \/  \/ \___/|_|  \__,_|_|\___|')
        print(f'                         __/ |                               ')
        print(f'                        |___/                               ')
        print(f'                                 \     /')
        print(f'                             \    o ^ o    /')
        print(f'                               \ (     ) /')
        print(f'                    ____________(%%%%%%%)____________')
        print(f'                   (     /   /  )%%%%%%%(  \   \     )')
        print(f'                   (___/___/__/           \__\___\___)')
        print(f'                      (     /  /(%%%%%%%)\  \     )')
        print(f'                       (__/___/ (%%%%%%%) \___\__)')
        print(f'                               /(       )\ ')
        print(f'                             /   (%%%%%)   \ ')
        print(f'                                  (%%%)')
        print(f'                                    ! \n')
        print(f"                            Welcome to Wordle!")
        print(f'                           ●▬▬▬▬๑▬▬▬▬▬๑▬▬▬▬▬● \n')
        print(f'                               How to play:')
        print(f'                           ●▬▬▬▬๑▬▬▬▬▬๑▬▬▬▬▬● \n')
        print(f"Guess the five-letter word by typing it into the terminal in {self.max_attempts} attempts.\n")
        print(f"          The game will then provide feedback for your guess:")
        print(f"A " + Fore.GREEN + "Green" + Style.RESET_ALL + " letter indicates that the letter is correct and in the correct position.")
        print(f"A " + Fore.YELLOW + "Yellow" + Style.RESET_ALL + " letter indicates that the letter is correct but in the wrong position.")
        print(f"A " + Fore.LIGHTBLACK_EX + "Gray" + Style.RESET_ALL + " letter indicates that the letter is incorrect and not in the word.")
        print(f'●▬▬▬▬๑▬▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬▬●\n')
        print(f"                Keep guessing until you find the correct word!")
        print(f'                         We hope you have fun!!!')
        print(f'               ●▬▬▬▬๑▬▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬๑▬▬▬▬▬●\n')

    def gameplay(self):
        secret_word = random.choice(self.words) #Chooses a random seceret word from the words list
        attempts = 0
        previous_guesses = set() #Uses sets instead of other list types because it ensures uniqueness and quick lookups of list items in comparison to other list types

        while attempts < self.max_attempts:
            guess = input(f"Enter your guess (attempt {attempts+1}/{self.max_attempts}): ").lower().strip()
            # Avoids any duplicate guesses being made.
            if guess in previous_guesses:
                print("You already guessed that word, try a different word.\n")
                continue
            previous_guesses.add(guess)

            feedback_obj = Feedback(secret_word, guess)
            
            #Validates the guess length and that the word is in the word list
            if not feedback_obj.is_valid_length():
                print("Your guess must be exactly 5 letters.\n")
                continue
            if not feedback_obj.is_valid_word(self.words):
                print("Your guess must be a valid English word from our list.\n")
                continue

            #Compares the guesses that the user made to the secret word and then generate the feedback for the user.
            feedback = feedback_obj.compare_words()

            #Takes the generated feedback and then prints out the color-coded feedback for the user.
            ColorFeedback(feedback).print_feedback()

            attempts += 1 #Increase the counter on the attempt amount

            #The win condition - i.e. the guess matches the secret word.
            if guess == secret_word:
                print("Congratulations! You've guessed the word correctly!\n")
                break
        else:
            #What occurs when the maximum attempts are reached.
            print("\nSorry, you've used all attempts. The correct word was:", secret_word.upper(),"\n")

    def play(self):
        # Runs the loop for restarting the gameplay or ending the attempt.
        while True:
            self.print_instructions()
            self.gameplay()

            while True:
                try:
                    again = input("\nDo you want to play again? (yes/no): ").lower().strip()
                    if again not in ['y', 'yes', 'n', 'no']:
                        raise ValueError("Invalid input. Please enter yes or no.")
                    break  # Valid input, break this inner loop
                except ValueError as ve:
                    #except that is ran if an invalid ending or restarting input is given by the user
                    print(f"\n{ve}")

            if again in ['n', 'no']:
                print("\n   Thanks for playing!")
                print(f'●▬▬▬▬๑▬▬▬▬▬๑▬▬▬▬▬๑▬▬▬▬▬● \n')
                break