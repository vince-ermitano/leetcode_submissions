class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int left = 0;
        int right = 0;

        if (s.length() == 0) {
            return 0;
        }

        int longest = 0;

        char[] charArr = s.toCharArray();

        while (right < s.length()) {
            char currChar = charArr[right];
            if (!seen.contains(currChar)) {
                longest = Math.max(longest, right - left + 1);
            } else {
                while (seen.contains(currChar)) {
                    seen.remove(charArr[left]);
                    left++;
                }
            }
            right++;
            seen.add(currChar);
        }

        return longest;
    }
}