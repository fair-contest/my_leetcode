#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        init_tmp(rectangles);
        max_area(tmp);
        while (tmp.size() > 1) {
            ar.clear();
            for (pt_area j : tmp) {
                Solution::reOverlap(cur, j);
            }
            if (cmp_vec(tmp, ar)) break;
            max_area(ar);
            tmp = ar;
        }
        if (ar.size() > 1) {
            for (pt_area k : ar) {
                res += k.area;
            }
        }
        return res % 1000000007;
    }

private:
    struct pt_area { vector<int> p; long long area; };
    vector<pt_area> ar;
    vector<pt_area> tmp;
    vector<int> vect;
    pt_area pta = { {0, 0, 0, 0}, 0 };
    pt_area cur = { {0, 0, 0, 0}, 0 };
    long long fa = 0;
    long long fb = 0;
    long long maxarea = 0;
    long long res = 0;

    void init_tmp(vector<vector<int>>& arr) {
        for (vector<int> vi : arr) {
            pta.p = vi;
            pta.area = vect_area(vi);
            tmp.push_back(pta);
        }
    }

    void reOverlap(pt_area& a, pt_area& b) {
        if (a.p[0] <= b.p[0] && a.p[1] <= b.p[1] && a.p[2] >= b.p[2] && a.p[3] >= b.p[3]) { return; }
        else if (a.p[0] >= b.p[2] || a.p[1] >= b.p[3] || a.p[2] <= b.p[0] || a.p[3] <= b.p[1]) { ar.push_back(b); }
        else if (a.p[0] <= b.p[0] && a.p[2] >= b.p[2]) {
            if (a.p[1] > b.p[1]) {
                if (a.p[3] < b.p[3]) { push_vec(b.p[0], a.p[3], b.p[2], b.p[3]); push_vec(b.p[0], b.p[1], b.p[2], a.p[1]); }
                else { if (a.p[1] < b.p[3]) { push_vec(b.p[0], b.p[1], b.p[2], a.p[1]); } }
            }
            else { if (a.p[3] > b.p[1] && a.p[3] < b.p[3]) { push_vec(b.p[0], a.p[3], b.p[2], b.p[3]); } }
        }
        else if (a.p[1] <= b.p[1] && a.p[3] >= b.p[3]) {
            if (a.p[0] > b.p[0]) {
                if (a.p[2] < b.p[2]) { push_vec(a.p[2], b.p[1], b.p[2], b.p[3]); push_vec(b.p[0], b.p[1], a.p[0], b.p[3]); }
                else { if (a.p[0] < b.p[2]) { push_vec(b.p[0], b.p[1], a.p[0], b.p[3]); } }
            }
            else { if (a.p[2]<b.p[2] && a.p[2]>b.p[0]) { push_vec(a.p[2], b.p[1], b.p[2], b.p[3]); } }
        }
        else if (a.p[0] > b.p[0]) {
            if (a.p[3] > b.p[3]) {
                if (a.p[2] >= b.p[2]) { push_vec(b.p[0], b.p[1], b.p[2], a.p[1]); push_vec(b.p[0], a.p[1], a.p[0], b.p[3]); }
                else { push_vec(b.p[0], b.p[1], b.p[2], a.p[1]); push_vec(b.p[0], a.p[1], a.p[0], b.p[3]); push_vec(a.p[2], a.p[1], b.p[2], b.p[3]); }
            }
            else if (a.p[1] < b.p[1]) {
                if (a.p[2] >= b.p[2]) { push_vec(b.p[0], a.p[3], b.p[2], b.p[3]); push_vec(b.p[0], b.p[1], a.p[0], a.p[3]); }
                else { push_vec(b.p[0], a.p[3], b.p[2], b.p[3]); push_vec(b.p[0], b.p[1], a.p[0], a.p[3]); push_vec(a.p[2], b.p[1], b.p[2], b.p[3]); }
            }
            else { push_vec(b.p[0], b.p[1], a.p[0], b.p[3]); push_vec(a.p[0], a.p[3], b.p[2], b.p[3]); push_vec(a.p[0], b.p[1], b.p[2], a.p[1]); }
        }
        else {
            if (a.p[2] < b.p[2]) {
                if (a.p[3] > b.p[3]) { push_vec(b.p[0], b.p[1], b.p[2], a.p[1]); push_vec(a.p[2], a.p[1], b.p[2], b.p[3]); }
                else if (a.p[1] < b.p[1]) { push_vec(b.p[0], a.p[3], b.p[2], b.p[3]); push_vec(a.p[2], b.p[1], b.p[2], a.p[3]); }
                else { push_vec(b.p[0], b.p[1], a.p[2], a.p[1]); push_vec(a.p[2], b.p[1], b.p[2], b.p[3]); push_vec(b.p[0], a.p[3], a.p[2], b.p[3]); }
            }
        }
    }

    inline void push_vec(int& a, int& b, int& c, int& d) {
        pta.p = {a, b, c, d};
        pta.area = vect_area(pta.p);
        ar.push_back(pta);
    }

    long long vect_area(vector<int>& x) {
        fa = x[2];
        fa -= x[0];
        fb = x[3];
        fb -= x[1];
        fa *= fb;
        if (fa >= 0) { return fa; }
        else { return -fa; }
    }

    inline void max_area(vector<pt_area>& x) {
        pta = { {0, 0, 0, 0}, 0 };
        for (int i = 0; i < x.size(); i++) {
            pta = (x[i].area > pta.area) ? x[i] : pta;
        }
        cur = pta;
        res += cur.area;
    }

    inline bool cmp_vec(vector<pt_area>& a, vector<pt_area>& b) {
        if (a.size() != b.size()) return false;
        for (int q = 0; q < a.size();q++) {
            if (a[q].p != b[q].p) return false;
        }
        return true;
    }
};
