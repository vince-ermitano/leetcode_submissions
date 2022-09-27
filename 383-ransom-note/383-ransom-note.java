class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] mag = magazine.toCharArray();
        char[] ransom = ransomNote.toCharArray();
        
        HashMap<Character, Integer> charCounts = new HashMap<Character, Integer>();
        
        for (char c : mag) {
            if (charCounts.containsKey(c)) {
                charCounts.replace(c, charCounts.get(c) + 1);
            } else {
                charCounts.put(c, 1);
            }
        }
        
        for (char c : ransom) {
            if (!charCounts.containsKey(c) || charCounts.get(c) <= 0) {
                return false;
            } else {
                charCounts.replace(c, charCounts.get(c) - 1);
            }
        }
        return true;
    }
}