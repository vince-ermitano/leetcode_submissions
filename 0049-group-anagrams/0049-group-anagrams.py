class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            groups[sorted_str].append(strs[i])
            
        print(groups)
            
        return [groups[key] for key in groups.keys()]
        