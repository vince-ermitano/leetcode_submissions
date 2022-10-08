class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counts = {}
        
        left = 0
        right = 0
        
        ans = 0
        
        while (right < len(s)):
            curr_char = s[right]
            counts[curr_char] = counts.get(curr_char, 0) + 1
            
            while (counts[curr_char] > 1):
                remove_char = s[left]
                counts[remove_char] -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            right+=1
        
        return ans
            
        
        