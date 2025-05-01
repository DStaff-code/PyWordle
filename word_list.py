#Initializes the words text file where secert words are pulled from
class Wordlist:
    def __init__(self, filename):
        self.filename = filename
        self.words = self.load_words()

    def load_words(self):
        #loads the words from the text file into the program to be used
        with open(self.filename, 'r') as file:
            #Strips newlines, then filters for all words that are exactly five-letters and finally appends them into a list
            words = []
            for line in file:
                word = line.strip().lower()
                if len(word) == 5:
                    words.append(word)
        return words

    
    def get_words(self):
        #encapsulates and prevents accidental mutation of words list for later calls
        return self.words
    

# if __name__ == "__main__":
#     wordlist = Wordlist("words.txt")
#     words = wordlist.get_words()
    
#     print("List of 5-letter words:")
#     for index, word in enumerate(words, start=1):
#         print(f"{index:4}: {word}")