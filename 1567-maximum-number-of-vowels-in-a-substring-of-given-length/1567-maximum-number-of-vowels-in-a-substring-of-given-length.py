class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        l = 0
        curr = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for r in range(len(s)):
            if s[r] in vowels:
                curr += 1

            if r+1 >= k:
                res = max(res, curr)

                if s[l] in vowels:
                    curr -= 1

                l += 1
        
        return res
            