# Notes

# Idea/Approach
* For every valley in the graph, just find the highest peak to the right of that valley. If encountering a valley smaller than any that you have already seen, just update the value of the valley.

# Complexity
* Time complexity is *O(N)* since we just need to pass the array of values once.
* Space complexity is *O(1)* since we just need to keep track of a couple variables to maintain the minVal and maxProfit
