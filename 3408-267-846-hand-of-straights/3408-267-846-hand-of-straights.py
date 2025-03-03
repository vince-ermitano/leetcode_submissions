class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        hand.sort()

        for num in hand:
            if counts[num]:
                for i in range(num, num + groupSize):
                    if counts[i] <= 0:
                        return False
                    counts[i] -= 1
        
        return True
        