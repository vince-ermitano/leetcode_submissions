class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # count each value and store in hashmap
        # loop through hashmap and store each count
        # in a set
        # if a count is encountered that already exists
        # in the set, return False

        counts = defaultdict(int)
        count_set = set()

        for n in arr:
            counts[n] += 1

        for v in counts.values():
            if v in count_set:
                return False
            
            count_set.add(v)

        return True
