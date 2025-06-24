class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        List<Integer>[] buckets = new List[nums.length+1];

        for (int i = 0; i < buckets.length; i++) {
            buckets[i] = new ArrayList<Integer>();
        }

        // count frequency of each distinct element
        for (int n : nums) {
            counts.put(n, counts.getOrDefault(n, 0) + 1);
        }

        // put each distinct element into their respective buckets (frequencies)
        for (int c : counts.keySet()) {
            buckets[counts.get(c)].add(c);
        }

        int[] res = new int[k];
        int index = 0;

        // loop through buckets in reverse order to find top k frequent elements
        for (int i = buckets.length-1; i > 0; i--) {
            for (int n: buckets[i]) {
                res[index++] = n;
                
                if (index == k) return res;
            }
        }

        return res;

    }
}