# Notes

## Idea
* Greedy approach
* Traverse through intervals (remember they are sorted by start times)
* Add all the intervals that start before the new interval starts.
* For the remaining intervals to be dealt with (including the new interval):
  * If the last added interval ends after the next current interval, merge the two intervals.
  * Else, this means there is no time conflict so we can just add the current interval to the answer.

## Complexity
* Time complexity is *O(N)*
* Space complexity is *O(N)*
