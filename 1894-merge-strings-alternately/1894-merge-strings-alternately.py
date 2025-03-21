class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = ptr2 = 0
        res = ""

        while (ptr1 < len(word1) and ptr2 < len(word2)):
            res += word1[ptr1] + word2[ptr2]
            ptr1 += 1
            ptr2 += 1
        
        if ptr1 < len(word1):
            res += word1[ptr1:]
        if ptr2 < len(word2):
            res += word2[ptr2:]

        return res


        