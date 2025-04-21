# Insert all products into a trie
# Sort product lexicographically
# As we insert these products, at each char we insert, add the next lexicographiclly
# ordered product to that node's suggestions, capping the suggestions to a limit of 3
# As we traverse searchWord (each of it's characters), we just return the node's suggestions
# at that point.

class Node:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # initialize trie
        root = Node()

        # sort products
        products.sort()

        # add products into trie and insert suggestions as we traverse
        for w in products:
            curr = root

            for char in w:
                if char not in curr.children:
                    curr.children[char] = Node()
                curr = curr.children[char]

                if len(curr.suggestions) < 3:
                    curr.suggestions.append(w)
        
        curr = root
        res = []

        # traverse through searchWord and return its suggestions at each char
        for char in searchWord:
            if curr and char in curr.children:
                curr = curr.children[char]
                res.append(curr.suggestions)
            else:
                curr = None
                res.append([])

        return res
            
        