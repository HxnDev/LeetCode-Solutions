#include<stack>
class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        int a = s.length();
        int b = 0;
        map<char, char> pairs{{')', '('}, {'}', '{'}, {']', '['}};
        while (b < a) {
            if (s[b] == '(' || s[b] == '{' || s[b] == '[') {
                stack.push(s[b]);
            } else {
                if (stack.empty() || stack.top() != pairs[s[b]]) {
                    return false;
                }
                stack.pop();
            }
            b++;
        }
        return stack.empty();
    }
};
