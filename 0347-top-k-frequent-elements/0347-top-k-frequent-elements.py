class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        
        seen = [[] for i in range(len(nums)+1)]
        counts = defaultdict(int)
        
        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        for num, count in counts.items():
            seen[count].append(num)
            
        ans = []
        
        
        for i in range(len(seen)-1, 0, -1):
            for num in seen[i]:
                ans.append(num)
                
                if len(ans) == k:
                    return ans
                        
        