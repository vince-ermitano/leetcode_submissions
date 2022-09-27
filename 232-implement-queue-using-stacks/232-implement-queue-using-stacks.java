class MyQueue {
    Stack<Integer> inOrderSt;
    Stack<Integer> regSt;

    public MyQueue() {
        inOrderSt = new Stack<Integer>();
        regSt = new Stack<Integer>();
    }
    
    public void push(int x) {
        regSt.push(x);
    }
    
    public int pop() {
        if (!inOrderSt.isEmpty()) {
            return inOrderSt.pop();
        }
        while (!regSt.isEmpty()) {
            inOrderSt.push(regSt.pop());
        }
        return inOrderSt.pop();
    }
    
    public int peek() {
        if (!inOrderSt.isEmpty()) {
            return inOrderSt.peek();
        }
        while (!regSt.isEmpty()) {
            inOrderSt.push(regSt.pop());
        }
        return inOrderSt.peek();
    }
    
    public boolean empty() {
        if (inOrderSt.isEmpty() && regSt.isEmpty()) {
            return true;
        }
        return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */