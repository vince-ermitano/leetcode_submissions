class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        ArrayList<int[]> ans = new ArrayList<int[]>();
        int lastAdded = 0;
        
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i][0] < newInterval[0]) {
                ans.add(intervals[i]);
                lastAdded = i;
            } else {
                break;
            }
        }
        
        if (ans.isEmpty() || ans.get(ans.size() - 1)[1] < newInterval[0]) {
            ans.add(newInterval);
        } else {
            ans.get(ans.size()-1)[1] = Math.max(newInterval[1], ans.get(ans.size()-1)[1]);
        }
        
        for (int i = lastAdded; i < intervals.length; i++) {
            if (ans.get(ans.size()-1)[1] < intervals[i][0]) {
                ans.add(intervals[i]);
            } else {
                ans.get(ans.size()-1)[1] = Math.max(intervals[i][1], ans.get(ans.size()-1)[1]);
            }
        }
        return ans.toArray(new int[ans.size()][2]);
    }
}