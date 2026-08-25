class Solution { 
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for (int i = 0; i < tokens.size(); i++) {
            if (tokens[i] == "+") {
                int a, b;
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                st.push(a + b);
            }
            else if (tokens[i] == "-") {
                int a, b;
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                st.push(a - b);
            }
            else if (tokens[i] == "*") {
                int a, b;
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                st.push(a * b);
            }
            else if (tokens[i] == "/") {
                int a, b;
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                st.push(a / b);
            }
            else {
                st.push(stoi(tokens[i]));
            }
        }
        return st.top();
    }
};