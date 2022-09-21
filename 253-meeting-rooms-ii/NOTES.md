# Notes

## Idea / Approach
* Approach with a greedy algorithm
* Any time a meeting is done using a room we will check if a meeting (with the earliest starting time following) can occupy that room. If not...
* Any time a meeting overlaps with another meeting, then we must obviously allocate another room.  

## Time/Space Complexity
* Utilizes priority queue where it can hold/store *n* meeting rooms so *O(nlogn)*
* Also sort time intervals at beginning for *n* meeting rooms so also *O(nlogn)*
* So overall time complexity is *O(nlogn)*

* Just need space to store *n* meetings in priority queue so *O(n)*
