class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # sort in nums2 in descending order, maintaining the index order
        # with nums1
        # build a prefix sum with the numbers from nums1 as we build our subsequence
        # adding these numbers into a minheap
        # when subsequence is of length, k, multiply by the number in nums2 that we
        # are currently looking at since this is guaranteed to be the smallest.
        # pop from minheap to maintain k length and remove the smallest number from our
        # prefix

        res, prefix_sum = 0, 0
        min_heap = []
        heapq.heapify(min_heap)

        # zip and sort by nums2 in desc order
        nums = list(zip(nums1, nums2))
        nums.sort(key=lambda x: x[1], reverse=True)

        for a, b in nums:
            prefix_sum += a
            heapq.heappush(min_heap, a)

            if len(min_heap) == k:
                res = max(res, prefix_sum * b)
                prefix_sum -= heapq.heappop(min_heap)
        
        return res