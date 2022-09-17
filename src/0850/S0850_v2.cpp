#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        vector<vector<int>> ar(200);
        vector<vector<int>> tmp = rectangles;
        const int MOD = 1e9 + 7;
        long long res = 0;
        while (tmp.size() != 0) {
            vector<int> m = max_area(tmp, res);
            ar.clear();
            for (vector<int> j : tmp) {
                Solution::reOverlap(m, j, ar);
            }
            tmp.clear();
            for (vector<int> k : ar) {
                push_vec(tmp, k[0], k[1], k[2], k[3]);
            }
        }
        if (ar.size() == 0) {
            return res % MOD;
        }
        else {
            return (res + Solution::vect_area(ar[0])) % MOD;
        }
    }

    void reOverlap(vector<int> a, vector<int> b, vector<vector<int>>& v) {
        if (a[0] <= b[0] && a[1] <= b[1] && a[2] >= b[2] && a[3] >= b[3]) { return; }
        else if (a[0] >= b[2] || a[1] >= b[3] || a[2] <= b[0] || a[3] <= b[1]) { v.push_back(b); }
        else if (a[0] <= b[0] && a[2] >= b[2]) {
            if (a[1] > b[1]) {
                if (a[3] < b[3]) { push_vec(v, b[0], a[3], b[2], b[3]); push_vec(v, b[0], b[1], b[2], a[1]); }
                else { if (a[1] < b[3]) { push_vec(v, b[0], b[1], b[2], a[1]); } }
            }
            else { if (a[3] > b[1] && a[3] < b[3]) { push_vec(v, b[0], a[3], b[2], b[3]); } }
        }
        else if (a[1] <= b[1] && a[3] >= b[3]) {
            if (a[0] > b[0]) {
                if (a[2] < b[2]) { push_vec(v, a[2], b[1], b[2], b[3]); push_vec(v, b[0], b[1], a[0], b[3]); }
                else { if (a[0] < b[2]) { push_vec(v, b[0], b[1], a[0], b[3]); } }
            }
            else { if (a[2]<b[2] && a[2]>b[0]) { push_vec(v, a[2], b[1], b[2], b[3]); } }
        }
        else if (a[0] > b[0]) {
            if (a[3] > b[3]) {
                if (a[2] >= b[2]) { push_vec(v, b[0], b[1], b[2], a[1]); push_vec(v, b[0], a[1], a[0], b[3]); }
                else { push_vec(v, b[0], b[1], b[2], a[1]); push_vec(v, b[0], a[1], a[0], b[3]); push_vec(v, a[2], a[1], b[2], b[3]); }
            }
            else if (a[1] < b[1]) {
                if (a[2] >= b[2]) { push_vec(v, b[0], a[3], b[2], b[3]); push_vec(v, b[0], b[1], a[0], a[3]); }
                else { push_vec(v, b[0], a[3], b[2], b[3]); push_vec(v, b[0], b[1], a[0], a[3]); push_vec(v, a[2], b[1], b[2], b[3]); }
            }
            else { push_vec(v, b[0], b[1], a[0], b[3]); push_vec(v, a[0], a[3], b[2], b[3]); push_vec(v, a[0], b[1], b[2], a[1]); }
        }
        else {
            if (a[2] < b[2]) {
                if (a[3] > b[3]) { push_vec(v, b[0], b[1], b[2], a[1]); push_vec(v, a[2], a[1], b[2], b[3]); }
                else if (a[1] < b[1]) { push_vec(v, b[0], a[3], b[2], b[3]); push_vec(v, a[2], b[1], b[2], a[3]); }
                else { push_vec(v, b[0], b[1], a[2], a[1]); push_vec(v, a[2], b[1], b[2], b[3]); push_vec(v, b[0], a[3], a[2], b[3]); }
            }
        }
    }

    void push_vec(vector<vector<int>>& arr, int a, int b, int c, int d) {
        vector<int> vect(4);
        vect[0] = a;
        vect[1] = b;
        vect[2] = c;
        vect[3] = d;
        arr.push_back(vect);
    }

    long long vect_area(vector<int>& x) {
        long long a = x[2];
        a -= x[0];
        long long b = x[3];
        b -= x[1];
        a *= b;
        if (a >= 0) { return a; }
        else { return -a; }
    }

    vector<int> max_area(vector<vector<int>>& x, long long& res) {
        vector<int> max(4);
        for (vector<int> v : x) {
            max = (vect_area(v) > vect_area(max)) ? v : max;
        }
        res += vect_area(max);
        return max;
    }
};

vector<vector<int>> arr_to_vec(int arr[3][4]) {
    vector<vector<int>> tmp;
    vector<int> s;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            s.push_back(arr[i][j]);
        }
        tmp.push_back(s);
    }
    return tmp;
}

int main(int argc, char* argv[])
{
    int ary[3][4] = { {1, 1, 4, 4}, {0, 1, 6, 2},{2, 0, 3, 11} };
    vector<vector<int>> vect = arr_to_vec(ary);
    Solution soho;
    std::cout << soho.rectangleArea(vect);
    return 0;
}
