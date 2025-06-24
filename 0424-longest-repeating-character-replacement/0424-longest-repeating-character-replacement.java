class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> count = new HashMap<>();
        int l = 0;
        int maxFreq = 0;
        int longest = 0;

        for (int r = 0; r < s.length(); r++) {
            count.put(s.charAt(r), count.getOrDefault(s.charAt(r), 0) + 1);
            maxFreq = Math.max(maxFreq, count.get(s.charAt(r)));

            while (r - l + 1 - maxFreq > k) {
                count.put(s.charAt(l), count.get(s.charAt(l))-1);
                l++;
            }

            longest = Math.max(longest, r - l + 1);
        }

        return longest;
    }
}