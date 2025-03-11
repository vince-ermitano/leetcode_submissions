class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # What we can infer:
        # - if str1 + str2 != str2 + str1, there is not gcd
        # - elif len(str1) > len(str2), str2 must be a prefix to str1
        # - elif len(str2) > len(str1), str1 must be a prefix to str2
        # - else the string lengths are equal so str1/str2 is the gcd
        
        if str1 + str2 != str2 + str1:
            return ""
        elif len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        elif len(str2) > len(str1):
            return self.gcdOfStrings(str2[len(str1):], str1)
        else:
            return str1