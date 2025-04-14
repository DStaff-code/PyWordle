#initializing wordlist
class Wordlist:
    def __init__(self, filename):
        self.filename = filename
        self.words = self.load_words()

    def load_words(self):
        with open(self.filename, 'r') as file:
            # Strip newlines and filter for exactly five-letter words
            words = []
            for line in file:
                word = line.strip().lower()
                if len(word) == 5:
                    words.append(word)
        return words

    
    def get_words(self):
        return self.words