class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        partition = []

        def backtrack(i):
            if i >= len(s):
                res.append(partition[:])
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i:j+1])
                    backtrack(j+1)
                    partition.pop()
        
        backtrack(0)

        return res

    def isPalindrome(self, word, l, r):

        while (l < r):
            if word[l] != word[r]:
                return False
            
            l, r = l+1, r-1
        
        return True

        