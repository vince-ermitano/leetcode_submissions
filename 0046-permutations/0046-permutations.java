class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        backtrack(0, nums);
        return res;
    }

    private void backtrack(int i, int[] nums) {
        if (i == nums.length) {
            List<Integer> perm = new ArrayList<>();
            for (int n : nums) {
                perm.add(n);
            }
            res.add(perm);
            return;
        }

        for (int j = i; j < nums.length; j++) {
            swap(nums, i, j);
            backtrack(i+1, nums);
            swap(nums, i, j);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}