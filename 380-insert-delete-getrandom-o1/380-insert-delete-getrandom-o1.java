class RandomizedSet {
    ArrayList<Integer> list;
    HashMap<Integer, Integer> map;
    Random rand = new Random();
    

    public RandomizedSet() {
        list = new ArrayList<Integer>();
        map = new HashMap<Integer, Integer>();
    }
    
    public boolean insert(int val) {
        if (this.map.containsKey(val)) {
            return false;
        }
        this.list.add(val);
        this.map.put(val, list.size() - 1);
        return true;
    }
    
    public boolean remove(int val) {
        if (!this.map.containsKey(val)) {
            return false;
        }
        int indexToBeRemoved = this.map.get(val);
        int lastNum = this.list.get(list.size() - 1);
        this.list.set(indexToBeRemoved, lastNum);
        this.map.put(lastNum, indexToBeRemoved);
        this.list.remove(list.size() - 1);
        this.map.remove(val);
        
        return true;
    }
    
    public int getRandom() {
        return this.list.get(rand.nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */