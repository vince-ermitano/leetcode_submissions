class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert both lists as sets
        # loop through both lists and add to resulting lists if not in
        # the other's set
        
        set1 = set(nums1)
        set2 = set(nums2)

        res = []
        res1 = set()
        res2 = set()

        for n in nums1:
            if not n in set2:
                res1.add(n)

        for n in nums2:
            if not n in set1:
                res2.add(n)

        res.append(list(res1))
        res.append(list(res2))

        return res
        