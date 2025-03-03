class Solution:
    def countAndSay(self, n: int) -> str:

        res = "1"

        for i in range(n-1):
            res = self.RLE(res)
        
        return res
            

            
    
    def RLE(self, s):
        left = right = 0
        res = ""

        while (left < len(s)):
            curr = s[left]

            while right < len(s) and s[right] == curr:
                right += 1
            
            res += str(right - left) + curr
            left = right
        return res
