class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> st1 = new Stack<Character>();
        Stack<Character> st2 = new Stack<Character>();
        
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        
        for (char c : sArr) {
            if (c != '#') {
                st1.push(c);
            }
            else {
                if (!st1.isEmpty()) {
                    st1.pop();
                }
            }
        }
        
        for (char c : tArr) {
            if (c != '#') {
                st2.push(c);
            }
            else {
                if (!st2.isEmpty()) {
                    st2.pop();
                }
            }
        }
        
        while (!st1.isEmpty() && !st2.isEmpty()) {
            if (st1.pop() != st2.pop()) {
                return false;
            }
        }
        
        if (st1.isEmpty() && st2.isEmpty()) {
            return true;
        }
        return false;
    }
}