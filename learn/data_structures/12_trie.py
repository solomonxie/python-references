"""
12. Trie: Prefix tree used for efficient string retrieval.
It is commonly used for autocomplete and spell-checking applications.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self): self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


trie = Trie()
trie.insert("hello")
print(f"Inserted 'hello' into Trie. Root children: {
      list(trie.root.children.keys())}")
