class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # lengths must be equal
        # must contain the same characters (not necessarily the same counts)
        # if the counts of each character are the same, they are 'close'
        
        # check if lengths are equal
        # check if they contain the same characters
        # check if counts of *unique* characters are the same
        # if all pass, return True else False

        if len(word1) != len(word2):
            return False

        char_to_counts1 = defaultdict(int)
        char_to_counts2 = defaultdict(int)

        for i in range(len(word1)):
            char_to_counts1[word1[i]] += 1
            char_to_counts2[word2[i]] += 1
        
        if set(char_to_counts1.keys()) != set(char_to_counts2.keys()):
            return False
        
        unique_counts1 = []
        unique_counts2 = []

        for n in char_to_counts1.values():
            unique_counts1.append(n)

        for n in char_to_counts2.values():
            unique_counts2.append(n)

        unique_counts1.sort()
        unique_counts2.sort()

        for i in range(len(unique_counts1)):
            if unique_counts1[i] != unique_counts2[i]:
                return False
        
        return True