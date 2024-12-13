class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.isWord = True
        

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        # add words to Trie
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()
        
        
        # backtracking dfs function to explore all possible words from one cell
        def dfs(word, r, c, node):
            if (r < 0 or c < 0 or 
               r == ROWS or c == COLS or
               board[r][c] not in node.children or (r, c) in visited):
                return
            
            visited.add((r, c))
            
            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.isWord:
                res.add(word)
                
            dfs(word, r, c - 1, node)
            dfs(word, r, c + 1, node)
            dfs(word, r - 1, c, node)
            dfs(word, r + 1, c, node)
            
            visited.remove((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs("", r, c, root)
        
        return list(res)
        