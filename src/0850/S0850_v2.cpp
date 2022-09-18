#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        vector<vector<int>> ar(50);
        vector<vector<int>> tmp(50);
        tmp = rectangles;
        max_area(tmp, res);
        while (ar.size() != 0) {
            ar.clear();
            for (vector<int> j : tmp) {
                Solution::reOverlap(maxarea, j, ar);
            }
            max_area(ar, res);
            if (tmp == ar) break;
            tmp = ar;
        }
        if (ar.size() != 0) {
            for (vector<int> k : ar) {
                res += Solution::vect_area(k);
            }
        }
        return res % 1000000007;
    }

private:
    vector<int> maxarea;
    vector<int> vect;
    long long res = 0;

    void reOverlap(vector<int>& a, vector<int>& b, vector<vector<int>>& v) {
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

    inline void push_vec(vector<vector<int>>& arr, int& a, int& b, int& c, int& d) {
        vect = { a, b, c, d };
        arr.push_back(vect);
    }

    static inline long long vect_area(vector<int>& x) {
        static long long fa;
        static long long fb;
        fa = x[2];
        fa -= x[0];
        fb = x[3];
        fb -= x[1];
        fa *= fb;
        if (fa >= 0) { return fa; }
        else { return -fa; }
    }

    inline void max_area(vector<vector<int>>& x, long long& res) {
        maxarea = { 0, 0, 0, 0 };
        for (int i = 0; i < x.size(); i++) {
            maxarea = (vect_area(x[i]) > vect_area(maxarea)) ? x[i] : maxarea;
        }
        res += vect_area(maxarea);
    }
};
