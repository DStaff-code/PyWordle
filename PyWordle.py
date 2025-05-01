from Gameplay import WordleGameplay
#Main file to be ran - starts the gameplay and calls the word text file

if __name__ == "__main__":
    game = WordleGameplay("words.txt")
    game.play()