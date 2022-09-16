/*
    原创算法
    这个算法的思路是将每一个矩形A依次与下一个比对后， 切割出除A以外的不相交的矩形（根据相交状况会是1-3个，最多3个）。 
    然后就可以直接保存A的面积， 并将每次比对后与A不相交的1-3个矩形集中放回到一个数组里， 全部比对后， 再从数组里取下一个矩形“A”，
    一直循环比对到数组中所有矩形都不相交， 即可将这个数组所有矩形面积累加求和。
    在上面思路的基础上，一个显而易见的优化性能的思路， 就是先对面积排序，从最大面积那个开始选A，因为最好的情况下，最大面积那个可能覆盖所有其它矩形，一下就出来答案。
    从另外一个角度来说，假如最大面积的矩形对其它矩形的覆盖率不高，其它矩形各自不相交的情况往往也会比较多，同样可以快速达成数组中矩形都不相交。 所以如此优化后，
    算法性能是非常高的，
    
    这个算法主要性能开销在排序上，这个思路的情况下，可以用rust自带的pdqsort， 最坏情况下的时间复杂度是O(n*lg n), 多数情况下，时间复杂度接近于O(n)
    所以我的算法时间复杂度是O(n*lg n)，实测很多时候性能是接近于O(n)的， 空间复杂度也是O(n), n为矩形个数。

*/
impl Solution {
    pub fn rectangle_area(rectangles: Vec<Vec<i32>>) -> i32 {
        let mut ar: Vec<(i32, i32, i32, i32)> = Vec::with_capacity(50);
        let mut tmp: Vec<(i32, i32, i32, i32, i64)> = Vec::with_capacity(50);
        let mut res = 0i64;
        for i in 0..rectangles.len() {
            tmp.push((rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3], Solution::vect_area(&rectangles[i])));
        }
        while ar.len() != 1 {
            tmp.sort_unstable_by_key(|x| x.4);
            let max_rect = match tmp.pop() {
                None => break,
                Some(x) => x,
            };
            res += max_rect.4;
            ar.clear();
            for j in tmp.iter() {
                Solution::reOverlap(&(max_rect.0, max_rect.1, max_rect.2, max_rect.3), &(j.0, j.1, j.2, j.3), &mut ar);
            }
            tmp.clear();
            for k in ar.iter() {
                tmp.push((k.0, k.1, k.2, k.3, Solution::rect_area(k)));
            }
        }
        res = if ar.is_empty() {res % (10i64.pow(9)+7)} else {ar.iter().map(|x|Solution::rect_area(x)).fold(res, |acc, x| acc + x) % (10i64.pow(9)+7)};
        res as i32
    }

    fn reOverlap(a: &(i32,i32,i32,i32), b: &(i32,i32,i32,i32), v: &mut Vec<(i32, i32, i32, i32)>) {
        // 计算是否两个矩形相交， 并返回除a以外的矩形（分割好后的）
        if a.0<=b.0 && a.1<=b.1 && a.2>=b.2 && a.3>=b.3 {return;} // x包含y
        else if a.0>=b.2 || a.1>=b.3 || a.2<=b.0 || a.3<=b.1 {v.push(*b);} // x和y互无覆盖
        else if a.0<=b.0 && a.2>=b.2 {
            if a.1>b.1 {
                if a.3<b.3 {v.push((b.0, a.3, b.2, b.3)); v.push((b.0, b.1, b.2, a.1));}
                else {if a.1<b.3 {v.push((b.0, b.1, b.2, a.1));}}
            } else {if a.3>b.1 && a.3<b.3 {v.push((b.0, a.3, b.2, b.3));}}
        }
        else if a.1<=b.1 && a.3>=b.3 {
            if a.0>b.0 {
                if a.2<b.2 {v.push((a.2, b.1, b.2, b.3)); v.push((b.0, b.1, a.0, b.3));}
                else {if a.0<b.2 {v.push((b.0, b.1, a.0, b.3));}}
            } else {if a.2<b.2 && a.2>b.0 {v.push((a.2, b.1, b.2, b.3));}}
        }
        else if a.0>b.0 {
            if a.3>b.3 {
                if a.2>=b.2 {v.push((b.0, b.1, b.2, a.1)); v.push((b.0, a.1, a.0, b.3));}
                else {v.push((b.0, b.1, b.2, a.1)); v.push((b.0, a.1, a.0, b.3)); v.push((a.2, a.1, b.2, b.3));}
            }
            else if a.1<b.1 {
                if a.2>=b.2 {v.push((b.0, a.3, b.2, b.3)); v.push((b.0, b.1, a.0, a.3));}
                else {v.push((b.0, a.3, b.2, b.3)); v.push((b.0, b.1, a.0, a.3)); v.push((a.2, b.1, b.2, b.3));}
            } else {v.push((b.0, b.1, a.0, b.3)); v.push((a.0, a.3, b.2, b.3)); v.push((a.0, b.1, b.2, a.1));}
        }
        else {
            if a.2<b.2 {
                if a.3>b.3 {v.push((b.0, b.1, b.2, a.1)); v.push((a.2, a.1, b.2, b.3));}
                else if a.1<b.1 {v.push((b.0, a.3, b.2, b.3)); v.push((a.2, b.1, b.2, a.3));}
                else {v.push((b.0, b.1, a.2, a.1)); v.push((a.2, b.1, b.2, b.3)); v.push((b.0, a.3, a.2, b.3));}
            }
        }
    }

    fn rect_area(x: &(i32, i32, i32, i32)) -> i64 {
        let x = (x.2-x.0) as i64 * (x.3-x.1) as i64;
        if x >= 0 {x} else {-x}
    }

    fn vect_area(x: &Vec<i32>) -> i64 {
        let x = (x[2]-x[0]) as i64 * (x[3]-x[1]) as i64;
        if x >= 0 {x} else {-x}
    }
}
