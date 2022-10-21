class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        
        for i in range(0, len(word)):
            if current_node.contains_next_char(word[i]) == False:
                current_node.put(word[i])
            current_node = current_node.get(word[i])
            
        current_node.set_end()
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current_node = self.search_prefix(word)
        
        if current_node is None:
            return False
        return current_node.is_end
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        return self.search_prefix(prefix) is not None
        
        
    def search_prefix(self, word):
        current_node = self.root
        
        for i in range(len(word)):
            if (current_node.contains_next_char(word[i])):
                current_node = current_node.get(word[i])
            else:
                return None
        
        return current_node
    
class TrieNode:
        
        def __init__(self):
            self.next_chars = [None] * 26
            self.is_end = False
        
        def contains_next_char(self, ch):
            return self.next_chars[string.ascii_lowercase.index(ch)] is not None
        
        def get(self, ch):
            return self.next_chars[string.ascii_lowercase.index(ch)]
        
        def put(self, ch):
            new_node = TrieNode()
            self.next_chars[string.ascii_lowercase.index(ch)] = new_node
        
        def set_end(self):
            self.is_end = True
        
            
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)