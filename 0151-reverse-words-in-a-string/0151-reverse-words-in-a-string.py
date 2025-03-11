class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        words = s.split()

        for w in reversed(words):
            if res:
                res += " "
            res += w

        return res