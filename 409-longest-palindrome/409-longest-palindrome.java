class Solution {
    public int longestPalindrome(String s) {
        char[] arr = s.toCharArray();
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int ans = 0;
        
        for (char c : arr) {
            if (map.containsKey(c)) {
                map.replace(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        
        for (char c : map.keySet()) {
            ans += map.get(c) / 2 * 2;
            
            if (ans % 2 == 0 && map.get(c) % 2 == 1) {
                ans++;
            }
        }
        return ans;
    }
}