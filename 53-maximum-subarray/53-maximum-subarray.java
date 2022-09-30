class Solution {
    public int maxSubArray(int[] nums) {
        int currMax = nums[0];
        int currSum = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            if (currSum < 0) {
                currSum = nums[i];
            } else {
                currSum += nums[i];
            }
            currMax = Math.max(currSum, currMax);
        }
        
        return currMax;
    }
}