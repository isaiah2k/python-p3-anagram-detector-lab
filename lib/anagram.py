# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for word in word_list:
            if word.lower() != self.word and sorted(word.lower()) == self.sorted_word:
                matches.append(word)
        return matches