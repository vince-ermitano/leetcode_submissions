class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()

        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            
            for idx, val in enumerate(i):
                if i[idx] == target[idx]:
                    found.add(idx)
                

        return len(found) == 3