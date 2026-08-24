#include <vector>

class MinStack {
private:
    vector<int> stack;
    vector<int> minStack;
public:    
    void push(int val) {
        stack.push_back(val);
        if (minStack.empty() || minStack[minStack.size() - 1] > val) {
            minStack.push_back(val);
            return;
        }
        minStack.push_back(minStack[minStack.size() - 1]);
    }
    
    // ⬇️ will always be called on non-empty stacks

    void pop() {
        stack.pop_back();
        minStack.pop_back();
    }
    
    int top() {
        return stack[stack.size() - 1];
    }
    
    int getMin() {
        return minStack[minStack.size() - 1];
    }
};