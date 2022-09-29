class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
        int ans = -1;
        
        for (int n : nums) {
            if (count.containsKey(n)) {
                count.replace(n, count.get(n) + 1);
            } else {
                count.put(n, 1);
            }
        }
        
        for (int key : count.keySet()) {
            if (count.get(key) > nums.length / 2) {
                ans = key;
            }
        }
        
        return ans;
    }
}