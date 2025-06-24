class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) return "";

        Map<Character, Integer> tCounts = new HashMap<>();
        Map<Character, Integer> windowCounts = new HashMap<>();

        for (char c : t.toCharArray()) {
            tCounts.put(c, tCounts.getOrDefault(c, 0) + 1);
        }

        int have = 0;
        int need = tCounts.size();
        int l = 0;
        int[] boundaries = {-1, -1};
        int shortest = Integer.MAX_VALUE;

        for (int r = 0; r < s.length(); r++) {
            char currChar = s.charAt(r);
            windowCounts.put(currChar, windowCounts.getOrDefault(currChar, 0) + 1);

            if (tCounts.containsKey(currChar) && windowCounts.get(currChar).equals(tCounts.get(currChar))) {
                have++;
            }

            while (have == need) {
                if (r - l + 1 < shortest) {
                    shortest = r - l + 1;
                    boundaries[0] = l;
                    boundaries[1] = r;
                }

                char leftChar = s.charAt(l);
                windowCounts.put(leftChar, windowCounts.get(leftChar)-1);

                if (tCounts.containsKey(leftChar) && windowCounts.get(leftChar) < tCounts.get(leftChar)) {
                    have--;
                }
                l++;
            }
        }

        return shortest == Integer.MAX_VALUE ? "" : s.substring(boundaries[0], boundaries[1]+1);
    }
}