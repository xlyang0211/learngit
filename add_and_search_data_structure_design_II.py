__author__ = 'seany'

# This method use dfs to search the word list, to reduce complexity, dic tree (trie) is used to search the word;


class Trie:
    def __init__(self):
        self.leaves = {}
        self.is_word = False


class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = Trie()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c] = Trie()
            cur = cur.leaves[c]
        cur.is_word = True

    def show_word(self):
        cur = self.root
        self.get_word("", cur)

    def get_word(self, word, cur):
        if cur.is_word:
            print word
        for k in cur.leaves.keys():
            self.get_word(word + k, cur.leaves[k])

    def search(self, word):
        return self.judge_word_in(word, 0, self.root)

    def judge_word_in(self, word, index, cur):
        if index == len(word):
            return cur.is_word
        elif word[index] == ".":
            for i in cur.leaves:
                if self.judge_word_in(word, index + 1, cur.leaves[i]):
                    return True
            return False
        else:
            if word[index] in cur.leaves:
                return self.judge_word_in(word, index + 1, cur.leaves[word[index]])
            else:
                return False

if __name__ == "__main__":
    # Your WordDictionary object will be instantiated and called as such:
    wordDictionary = WordDictionary()
    wordDictionary.addWord("a")
    wordDictionary.addWord("a")
    # wordDictionary.addWord("")
    wordDictionary.show_word()
    # print wordDictionary.search(".a")
    # print wordDictionary.search("a")
    # print wordDictionary.search("a")
    print wordDictionary.search("a.")