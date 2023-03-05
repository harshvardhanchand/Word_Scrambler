
# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from .models import TrieNode,Trie,TrieNodeEncoder,TrieEncoder
import string
import itertools
import json

LETTERS = string.ascii_lowercase




def traverse_trie(node):
    """Traverse the trie recursively and return all words in it."""
    words = []
    for child_node in node.children.values():
        words.extend(child_node.words)
        words.extend(traverse_trie(child_node))
    return words

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
    root_node = TrieNode.objects.create(children={}, words=[])
    trie = Trie.objects.create(root=root_node)
    with open('/Users/harsh/Desktop/Word_Scrambler/assets/DL.txt') as f:
        for line in f:
            word = line.strip().lower()
            node = trie.root
            for char in word:
                if char not in node.children:
                    child_node = TrieNode.objects.create(children={}, words=[])
                    node.children[char] = child_node
                    node.save()
                node = node.children[char]
                node.words.append(word)
                node.save()
    return trie



def find_matches(word, trie):
    """Find all matches of a scrambled word in the trie."""
    node = trie.root
    for char in word:
        if char not in node.children:
            return []
        node = node.children[char]
    matches = []
    matches.extend(node.words)
    matches.extend(traverse_trie(node))
    return matches


def index(request):
    """View function that renders the home page with a word scrambler form."""
    if request.method == 'POST':
        word = request.POST['word']
        trie = load_dictionary()
        matches = find_matches(word, trie)
        return render(request, 'word_scrambler_app/results.html', {'matches': matches})
    else:
        return render(request, 'word_scrambler_app/index.html')



