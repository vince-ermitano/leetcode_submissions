class Solution {
    List<List<Integer>> result = new LinkedList();
    int n;
    int k;
    
    public List<List<Integer>> combine(int n, int k) {
        this.n = n;
        this.k = k;
        backtrack(1, new LinkedList<Integer>());
        return result;
    }
    
    public void backtrack(int start, LinkedList<Integer> curr) {
        if (curr.size() == k) {
            result.add(new LinkedList(curr));
            return;
        }
        if (start > n) {
            return;
        }

        curr.add(start);
        backtrack(start + 1, curr);
        curr.removeLast();
        backtrack(start + 1, curr);
    }
    
    private void printCurr(LinkedList<Integer> curr) {
        for (int i : curr) {
            System.out.print(i + ", ");
        }
    } 
}