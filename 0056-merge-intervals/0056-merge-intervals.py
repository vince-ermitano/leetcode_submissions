class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = []
        
        intervals.sort()
        print(intervals)
        
        for i in range(0, len(intervals)):
            if (len(merged) == 0 or intervals[i][0] > merged[-1][1]):
                merged.append(intervals[i])
            
            elif (intervals[i][0] <= merged[-1][1]):
                if (intervals[i][1] > merged[-1][1]):
                    merged[-1][1] = intervals[i][1]
            
        return merged