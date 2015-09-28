__author__ = 'seany'

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.word_list = set([])

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        self.word_list.add(word)
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        if word in self.word_list:
            return True
        else:
            new_word = ""
            return self.judge_word_in(word, 0, new_word, self.word_list)

    def judge_word_in(self, word, index, new_word, word_list):
        if index == len(word):
            if new_word in word_list:
                return True
        elif word[index] == ".":
            for i in self.alphabet:
                if self.judge_word_in(word, index+1, new_word + i, self.word_list):
                    return True
        else:
            if self.judge_word_in(word, index+1, new_word + word[index], self.word_list):
                return True
        return False

if __name__ == "__main__":
    # Your WordDictionary object will be instantiated and called as such:
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    wordDictionary.addWord("world")
    wordDictionary.addWord("wor")
    print wordDictionary.search("wor")