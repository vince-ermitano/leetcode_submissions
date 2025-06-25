class Solution {
    public List<List<Integer>> permute(int[] nums) {
        boolean[] chosen = new boolean[nums.length];
        List<List<Integer>> res = new ArrayList<>();
        dfs(new ArrayList<>(), nums, chosen, res);
        return res;
    }

    private void dfs(List<Integer> perm, int[] nums, boolean[] chosen, List<List<Integer>> res) {
        if (perm.size() == nums.length) {
            res.add(new ArrayList<>(perm));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!chosen[i]) {
                perm.add(nums[i]);
                chosen[i] = true;
                dfs(perm, nums, chosen, res);
                perm.remove(perm.size() - 1);
                chosen[i] = false;
            }
        }
    }
}