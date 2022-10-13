class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int rec[arr.size()+1];
        rec[0] = 0;
        int cur = arr[0];
        int p = 0;
        for (int i = 0; i < arr.size(); i++) {
            while (arr[i] < rec[p]) p--;
            if (arr[i] > cur) cur = arr[i];
            rec[++p] = cur;
        }
        return p;
    }
};
