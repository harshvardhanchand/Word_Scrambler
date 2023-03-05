import string
import itertools

# Define the alphabet letters
LETTERS = string.ascii_lowercase

class TrieNode:
    """A class representing a node in a trie data structure."""
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    """A class representing a trie data structure."""
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        
        """Insert a word into the trie."""
         
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)

    def search(self, word):
        """Search for a word in the trie and return a list of words that have the same letters."""
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words


def word_to_list(word):
    """Convert a word to a list of its characters."""
    return [char for char in word]

def list_to_word(lst):
    """Convert a list of characters to a word."""
    return ''.join(lst)

def generate_permutations(word):
    """Generate all possible permutations of a word."""
    return set([''.join(perm) for perm in itertools.permutations(word)])

def load_dictionary():
    """Load a dictionary file and build a trie data structure from it."""
    trie = Trie()
    with open('/Users/harsh/Desktop/Word Scrambler/assets/DL.txt') as f:
        for line in f:
            word = line.strip().lower()
            trie.insert(word)
    return trie

def find_matches(word, trie):
    """Find all words that have the same letters as the given word."""
    matches = []
    perms = generate_permutations(word_to_list(word))
    for perm in perms:
        words = trie.search(perm)
        if words:
            matches.extend(words)
    return matches

def main():
    """Main function that prompts the user to enter a scrambled word and prints all matching words."""
    trie = load_dictionary()
    while True:
        word = input("Enter a scrambled word: ").lower()
        matches = find_matches(word, trie)
        if matches:
            print(' '.join(matches))
        else:
            print('No match found')
        again = input("Try again? [Y/n]: ")
        if again.lower() == 'n':
            break

if __name__ == '__main__':
    main()
