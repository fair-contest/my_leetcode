#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        vector<tuple<int, int, int, int>> ar(200);
        vector<tuple<int, int, int, int, long long>> tmp(200);
        const int MOD = 1e9+7;
        long long res = 0;
        for (int i=0; i<rectangles.size(); i++) {
            tmp[i] = make_tuple(rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3], Solution::vect_area(rectangles[i]));
        }
        while (ar.size() != 1) {
            tuple<int, int, int, int, long long> m = max_area(tmp);
            res += get<4>(m);
            ar.clear();
            for (auto j : tmp) {
                Solution::reOverlap(make_tuple(get<0>(m), get<1>(m), get<2>(m), get<3>(m)), make_tuple(get<0>(j), get<1>(j), get<2>(j), get<3>(j)), ar);
            }
            tmp.clear();
            for (auto k : ar) {
                tmp.push_back(make_tuple(get<0>(k), get<1>(k), get<2>(k), get<3>(k), Solution::rect_area(k)));
            }
        }
        if (ar.size() == 0) {
            return res % MOD;
        } else {
            return (res + Solution::rect_area(ar[0])) % MOD;
        }
    }

    void reOverlap(tuple<int, int, int, int> a, tuple<int, int, int, int> b, vector<tuple<int, int, int, int>> &v) {
        if (get<0>(a)<=get<0>(b) && get<1>(a)<=get<1>(b) && get<2>(a)>=get<2>(b) && get<3>(a)>=get<3>(b)) {return;}
        else if (get<0>(a)>=get<2>(b) || get<1>(a)>=get<3>(b) || get<2>(a)<=get<0>(b) || get<3>(a)<=get<1>(b)) {v.push_back(b);}
        else if (get<0>(a)<=get<0>(b) && get<2>(a)>=get<2>(b)) {
            if (get<1>(a)>get<1>(b)) {
                if (get<3>(a)<get<3>(b)) {v.push_back(make_tuple(get<0>(b), get<3>(a), get<2>(b), get<3>(b))); v.push_back(make_tuple(get<0>(b), get<1>(b), get<2>(b), get<1>(a)));}
                else {if (get<1>(a)<get<3>(b)) {v.push_back(make_tuple(get<0>(b), get<1>(b), get<2>(b), get<1>(a)));}}
            } else {if (get<3>(a)>get<1>(b) && get<3>(a)<get<3>(b)) {v.push_back(make_tuple(get<0>(b), get<3>(a), get<2>(b), get<3>(b)));}}
        }
        else if (get<1>(a)<=get<1>(b) && get<3>(a)>=get<3>(b)) {
            if (get<0>(a)>get<0>(b)) {
                if (get<2>(a)<get<2>(b)) {v.push_back(make_tuple(get<2>(a), get<1>(b), get<2>(b), get<3>(b))); v.push_back(make_tuple(get<0>(b), get<1>(b), get<0>(a), get<3>(b)));}
                else {if (get<0>(a)<get<2>(b)) {v.push_back(make_tuple(get<0>(b), get<1>(b), get<0>(a), get<3>(b)));}}
            } else {if (get<2>(a)<get<2>(b) && get<2>(a)>get<0>(b)) {v.push_back(make_tuple(get<2>(a), get<1>(b), get<2>(b), get<3>(b)));}}
        }
        else if (get<0>(a)>get<0>(b)) {
            if (get<3>(a)>get<3>(b)) {
                if (get<2>(a)>=get<2>(b)) {v.push_back(make_tuple(get<0>(b), get<1>(b), get<2>(b), get<1>(a))); v.push_back(make_tuple(get<0>(b), get<1>(a), get<0>(a), get<3>(b)));}
                else {v.push_back(make_tuple(get<0>(b), get<1>(b), get<2>(b), get<1>(a))); v.push_back(make_tuple(get<0>(b), get<1>(a), get<0>(a), get<3>(b))); v.push_back(make_tuple(get<2>(a), get<1>(a), get<2>(b), get<3>(b)));}
            }
            else if (get<1>(a)<get<1>(b)) {
                if (get<2>(a)>=get<2>(b)) {v.push_back(make_tuple(get<0>(b), get<3>(a), get<2>(b), get<3>(b))); v.push_back(make_tuple(get<0>(b), get<1>(b), get<0>(a), get<3>(a)));}
                else {v.push_back(make_tuple(get<0>(b), get<3>(a), get<2>(b), get<3>(b))); v.push_back(make_tuple(get<0>(b), get<1>(b), get<0>(a), get<3>(a))); v.push_back(make_tuple(get<2>(a), get<1>(b), get<2>(b), get<3>(b)));}
            } else {v.push_back(make_tuple(get<0>(b), get<1>(b), get<0>(a), get<3>(b))); v.push_back(make_tuple(get<0>(a), get<3>(a), get<2>(b), get<3>(b))); v.push_back(make_tuple(get<0>(a), get<1>(b), get<2>(b), get<1>(a)));}
        }
        else {
            if (get<2>(a)<get<2>(b)) {
                if (get<3>(a)>get<3>(b)) {v.push_back(make_tuple(get<0>(b), get<1>(b), get<2>(b), get<1>(a))); v.push_back(make_tuple(get<2>(a), get<1>(a), get<2>(b), get<3>(b)));}
                else if (get<1>(a)<get<1>(b)) {v.push_back(make_tuple(get<0>(b), get<3>(a), get<2>(b), get<3>(b))); v.push_back(make_tuple(get<2>(a), get<1>(b), get<2>(b), get<3>(a)));}
                else {v.push_back(make_tuple(get<0>(b), get<1>(b), get<2>(a), get<1>(a))); v.push_back(make_tuple(get<2>(a), get<1>(b), get<2>(b), get<3>(b))); v.push_back(make_tuple(get<0>(b), get<3>(a), get<2>(a), get<3>(b)));}
            }
        }
    }

    long long rect_area(tuple<int, int, int, int>& x) {
        long long r = (get<2>(x) - get<0>(x));
        r *= (get<3>(x) - get<1>(x));
        if (r>=0) {return r;} else {return -r;}
    }

    long long vect_area(vector<int>& x){
        long long r = (x[2] - x[0]);
        r *= (x[3] - x[1]);
        if (r>=0) {return r;} else {return -r;}
    }

    tuple<int, int, int, int, long long> max_area(vector<tuple<int, int, int, int, long long>>& x) {
        tuple<int, int, int, int, long long> max;
        for (auto v : x) {
            max = (get<4>(v) > get<4>(max)) ? v : max;
        }
        return max;
    }
};
