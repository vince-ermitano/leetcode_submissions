class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = [[] for i in range(len(nums)+1)]
        
        counts = defaultdict(int)
        
        for i in range(len(nums)):
            counts[nums[i]] += 1
            
        print(counts)
        
        for key in counts.keys():
            seen[counts[key]].append(key)
            
        print(seen)
            
        collected = 0
        
        ans = []
        
        
        for i in range(len(seen)-1, -1, -1):
            print(i)
            if (collected < k):
                if len(seen[i]) == 0:
                    continue
                elif len(seen[i]) + collected <= k:
                    for num in seen[i]:
                        print(num)
                        ans.append(num)
                    
                    collected += len(seen[i])
                else:
                    for j in range(k-collected):
                        added = seen[i].pop()
                        print(added)
                        ans.append(added)
                    
                    collected += k - collected
        
        return ans
                        
        