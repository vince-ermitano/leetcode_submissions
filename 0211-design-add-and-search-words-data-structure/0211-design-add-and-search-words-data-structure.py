class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                
            curr = curr.children[c]
            
        curr.endOfWord = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        def dfs(j, root):
            
            curr = root
            
            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':
                    for potential in curr.children.values():
                        if dfs(i+1, potential):
                            return True
                    return False
                
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
             
            return curr.endOfWord
        
        return dfs(0, self.root)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)