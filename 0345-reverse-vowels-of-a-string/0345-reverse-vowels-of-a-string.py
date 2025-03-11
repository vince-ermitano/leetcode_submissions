class Solution:
    def reverseVowels(self, s: str) -> str:
        # extract the vowels and their indices
        # reverse the extracted vowels
        # insert reversed vowels in the unreversed indices

        # use two pointer
        # update l and r pointers until they
        # either cross -> terminate
        # or both are vowels -> swap

        chars = list(s)
        l, r = 0, len(chars) - 1
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        vowels = set(vowels)

        while l < r:
            if not chars[l] in vowels:
                l += 1
            if not chars[r] in vowels:
                r -= 1
            
            if l < r and chars[l] in vowels and chars[r] in vowels:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        
        return "".join(chars)