class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int m = l + ((r - l) / 2);

            if (nums[m] == target) {
                return m;
            }
            
            // left sorted portion
            if (nums[l] <= nums[m]) {
                if (target < nums[l]) {
                    l = m + 1;
                } else if (target > nums[m]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            } else { // right sorted portion
                if (target > nums[r]) {
                    r = m - 1;
                } else if (target < nums[m]) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }
        }

        return -1;
    }
}