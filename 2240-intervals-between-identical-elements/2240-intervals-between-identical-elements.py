class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        # Approach
        # Group indices by value in hashmap (i.e. val -> [array of indices where arr[i] == val])
        # Calculate the prefix sum of indices for each value
        # With the prefix sums, we can efficiently calculate the interval sums

        value_indices = defaultdict(list)
    
        # Group indices by value
        for i, val in enumerate(arr):
            value_indices[val].append(i)
        
        n = len(arr)
        result = [0] * n
        
        # For each group, calculate distances using prefix sums
        for indices in value_indices.values():
            k = len(indices)
            prefix_sum = list(accumulate(indices))
            
            for m, idx in enumerate(indices):
                # calculate intervals sum for indices < m
                left_sum = idx * m - (prefix_sum[m - 1] if m > 0 else 0)
                # calculate intervals sum for indices > m
                right_sum = (prefix_sum[-1] - prefix_sum[m]) - (k - m - 1) * idx

                # interval sum equals the total of the interval sums of for indices < m and indices > m
                result[idx] = left_sum + right_sum
        
        return result