import random
from colorama import Fore, Style


class Feedback:
    def __init__(self, secret_word, user_guess):
        self.secret_word = secret_word #The word to be guessed.
        self.user_guess = user_guess #The current guess entered by the player.

    def is_valid_length(self): 
        #Checks if the guess has exactly 5 letters.
        return len(self.user_guess) == 5

    def is_valid_word(self, word_list): 
        #Confirms that the guess is in the provided word list.
        return self.user_guess in word_list

    def compare_words(self): 
        #Compares each letter of the guess against the secret word and returns status for each letter: correct, present, or absent.
        result = []
        secret_list = list(self.secret_word)
        guess_list = list(self.user_guess)
        secret_checked = [False] * 5  #Used to track that the letters in the secret word which have been matched already.
        
        #Inital pass: marks letters that are in the correct position.
        for i in range(5):
            if guess_list[i] == secret_list[i]:
                result.append(('correct', guess_list[i]))
                secret_checked[i] = True
            else:
                result.append((None, guess_list[i]))

        # Second pass: marks the letters that are present but in the wrong position.
        for i in range(5):
            if result[i][0] is None:
                if guess_list[i] in secret_list:
                    found = False
                    #checks whether or not a letter from the user's guess, that is not in the correct position, still appears somewhere else in the secret word and hasn't already been matched before
                    for j in range(5):
                        if not secret_checked[j] and secret_list[j] == guess_list[i]:
                            found = True
                            secret_checked[j] = True
                            break
                    if found:
                        result[i] = ('present', guess_list[i])
                    else:
                        result[i] = ('absent', guess_list[i])
                else:
                    result[i] = ('absent', guess_list[i])
        return result

class ColorFeedback: 
#Colors the feedback provided by the Feedback class and then displays the result. 
    def __init__(self, feedback):
        self.feedback = feedback

    def print_feedback(self): 
    #Iterates through the feedback and prints each letter with its new color.
        colored_string = ""
        for status, letter in self.feedback:
            if status == 'correct':
                colored_string += Fore.GREEN + letter.upper() + " "
            elif status == 'present':
                colored_string += Fore.YELLOW + letter.upper() + " "
            else:
                colored_string += Fore.LIGHTBLACK_EX + letter.upper() + " "
        print(colored_string + Style.RESET_ALL, "\n")

# if __name__ == "__main__":
#     #secret word is 'apple' 
#     #user's guess is 'ample'
#     secret = "apple"
#     guess = "algin"
#     feedback_obj = Feedback(secret, guess)
#     result = feedback_obj.compare_words()
#     ColorFeedback(result).print_feedback()
