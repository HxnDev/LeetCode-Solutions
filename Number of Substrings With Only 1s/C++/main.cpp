

#define mod 1000000007

class Solution {
public:
    int numSub(string s) {
        int n = s.length(), res = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') {
            int l = i, r = i;
            while (r < n && s[r] == '1') {
                res = (res + r - l + 1) % mod;
                r++;
            }
            i = r - 1;
        }
    }
    return res;
    }
};
