class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # for each spell, find the weakest potion that fulfills the successful prop.
        # the number of pairs will be the amount of potions from the weakest successful potion
        # to the end (if the array is sorted), so we
        # sort the potions array
        # use binary search to find the weakest successful potion

        potions.sort()
        res = [0] * len(spells)

        for i in range(len(spells)):
            l, r = 0, len(potions) - 1

            while l <= r:
                m = (l + r) // 2

                if potions[m] * spells[i] >= success:
                    r = m - 1
                else:
                    l = m + 1
            
            res[i] = len(potions) - l

        
        return res