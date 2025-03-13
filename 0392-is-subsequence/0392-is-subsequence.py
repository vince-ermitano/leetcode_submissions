class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    
        ptr_s = ptr_t = 0

        while ptr_t < len(t) and ptr_s < len(s):
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1
        
        return ptr_s >= len(s)