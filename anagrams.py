# This is realized in C++, which does not store different groups of anagrams into different sub list;

class Solution {
public:
    vector<string> anagrams(vector<string> &strs) {
        string s;
        map<string, int> anagram;
        vector<string> res;
        for (int i = 0; i < strs.size(); ++i) {
            s = strs[i];
            sort(s.begin(), s.end());
            if (anagram.find(s) == anagram.end()) {
                anagram[s] = i;
            } else {
                if (anagram[s] >= 0) {
                    res.push_back(strs[anagram[s]]);
                    anagram[s] = -1;
                }
                res.push_back(strs[i]);
            }
        }
        return res;
    }
};