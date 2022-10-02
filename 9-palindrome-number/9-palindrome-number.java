class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || x % 10 == 0 && x != 0) {
            return false;
        }
        
        int reversedHalf = 0;
        
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }
        
        if (x == reversedHalf || x == reversedHalf / 10) {
            return true;
        }
        return false;
    }
}