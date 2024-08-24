from trie import Trie
from corrections import get_corrections

class SpellChecker:
    def __init__(self, dictionary_file):
        self.dictionary_trie = Trie()
        self.load_dictionary(dictionary_file)

    def load_dictionary(self, dictionary_file):
        with open(dictionary_file, 'r') as file:
            for word in file:
                word = word.strip().lower()
                self.dictionary_trie.insert(word)

    def check_word(self, word):
        word = word.lower()
        if self.dictionary_trie.search(word):
            return f"'{word}' is spelled correctly."
        else:
            suggestions = get_corrections(word, self.dictionary_trie)
            return f"'{word}' is misspelled. Did you mean: {', '.join(suggestions)}?"

    def check_text(self, text):
        words = text.split()
        results = []
        for word in words:
            result = self.check_word(word)
            results.append(result)
        return '\n'.join(results)

if __name__ == "__main__":
    spell_checker = SpellChecker('dictionary.txt')

    while True:
        text = input("Enter text to check (or 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        result = spell_checker.check_text(text)
        print(result)
