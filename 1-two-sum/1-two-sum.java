class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] ans = new int[2];
        
        for (int i = 0; i < nums.length; i++) {
            int numToFindInMap = target - nums[i];
            
            if (map.containsKey(numToFindInMap)) {
                ans[0] = map.get(numToFindInMap);
                ans[1] = i;
                break;
            }
            map.put(nums[i], i);
        }
        return ans;
    }
}