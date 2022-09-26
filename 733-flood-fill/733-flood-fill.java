class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) {
            return image;
        }
        recurse(image, image[sr][sc], color, sr, sc);
        return image;
    }
    
    private void recurse(int[][] image, int originalColor, int color, int row, int col) {
        
        if (row < 0 || col < 0 || row >= image.length || col >= image[0].length || image[row][col] != originalColor) {
            return;
        } else {
            image[row][col] = color;
            recurse(image, originalColor, color, row + 1, col);
            recurse(image, originalColor, color, row - 1, col);
            recurse(image, originalColor, color, row, col + 1);
            recurse(image, originalColor, color, row, col - 1);
        }
    }
}