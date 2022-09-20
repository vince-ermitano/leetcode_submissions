class Solution {
    public boolean isValid(String s) {
        //utilize stack to check if s is valid at every character read so far
        Stack<Character> st = new Stack<Character>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            //two general cases: opening type or closing type
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            else {
                if (st.isEmpty()) {
                    return false;
                }
                if (c == ')') {
                    if (st.pop() != '(') {
                        return false;
                    }
                } else if (c == '}') {
                    if (st.pop() != '{') {
                        return false;
                    }
                } else {
                    if (st.pop() != '[') {
                        return false;
                    }
                }
            }
        }
        
        //stack must be empty for valid parentheses
        if (!st.isEmpty()) {
            return false;
        }
        return true;
    }
}