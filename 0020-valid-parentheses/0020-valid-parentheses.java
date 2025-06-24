class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        Map<Character, Character> map = new HashMap<>();

        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');

        for (char p: s.toCharArray()) {
            if (map.containsKey(p)) {
                if (!st.isEmpty() && st.peek().equals(map.get(p))) {
                    st.pop();
                } else {
                    return false;
                }
            } else {
                st.push(p);
            }
        }

        return st.isEmpty();
    }
}