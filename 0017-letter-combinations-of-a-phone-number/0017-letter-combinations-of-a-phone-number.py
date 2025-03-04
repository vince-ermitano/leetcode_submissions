class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []
            
        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        curr = []

        def backtrack(i):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            
            for c in digits_to_letters[digits[i]]:
                curr.append(c)
                backtrack(i+1)
                curr.pop()
        
        backtrack(0)

        return res