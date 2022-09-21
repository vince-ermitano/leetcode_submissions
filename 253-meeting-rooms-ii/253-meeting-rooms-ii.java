class Solution {
    public int minMeetingRooms(int[][] intervals) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        for (int[] interval : intervals) {
            if (pq.isEmpty()) {
                pq.add(interval[1]);
            } else {
                //if new meeting overlaps with earliest ending meeting, then allocate new room
                if (interval[0] < pq.peek()) {
                    pq.add(interval[1]);
                }
                else {
                    pq.poll();
                    pq.add(interval[1]);
                }
            }
        }
        return pq.size();
    }
}