class Solution {
public:
    int minimumLength(string s) {
    	int i = 0, j = s.size() - 1;
    	while (i < j && s[i] == s[j])
    	{
    		do {i++;} while (i < j && s[i] == s[i-1]);
    		do {j--;} while (i <= j && s[j] == s[j+1]);
    	}
    	return j - i + 1;
    }
};
