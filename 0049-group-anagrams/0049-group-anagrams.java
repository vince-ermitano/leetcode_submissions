class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> hm = new HashMap<String, ArrayList<String>>();

        // loop through all strings and calculate composition "signature"
        for (String s: strs) {
            int[] count = new int[26];

            // find the frequencies of each char
            for (char c: s.toCharArray()) {
                count[c-'a'] += 1;
            }

            String key = Arrays.toString(count);
            
            // add s to matching signature list
            if (!hm.containsKey(key)) {
                hm.put(key, new ArrayList<String>());
            }
            hm.get(key).add(s);
        }

        return new ArrayList<>(hm.values());
    }
}