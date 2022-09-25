impl Solution {
    pub fn rectangle_area(rectangles: Vec<Vec<i32>>) -> i32 {
        if rectangles.len() == 1 {return (Solution::vect_area(&rectangles[0]) % 1000000007) as i32}
        let mut ar: Vec<(i32, i32, i32, i32)> = Vec::with_capacity(50);
        let mut tmp: Vec<(i32, i32, i32, i32, i64)> = Vec::with_capacity(50);
        let mut res = 0i64;
        for i in 0..rectangles.len() {
            tmp.push((rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3], Solution::vect_area(&rectangles[i])));
        }
        while tmp.len() > 1 {
            tmp.sort_unstable_by_key(|x| x.4);
            let max_rect = tmp.last().unwrap();
            res += max_rect.4;
            ar.clear();
            for j in tmp.iter() {
                Solution::reOverlap(&(max_rect.0, max_rect.1, max_rect.2, max_rect.3), &(j.0, j.1, j.2, j.3), &mut ar);
            }
            if Solution::ar_cmp_tmp(&ar, &tmp) {break;}
            tmp.clear();
            for k in ar.iter() {
                tmp.push((k.0, k.1, k.2, k.3, Solution::rect_area(k)));
            }
        }
        res = if ar.is_empty() {res % 1000000007} else { (res + tmp.iter().map(|x| x.4).sum::<i64>()) % 1000000007};
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

    fn ar_cmp_tmp(a: &Vec<(i32, i32, i32, i32)>, b: &Vec<(i32, i32, i32, i32, i64)>) -> bool {
        if a.len() != b.len() {
            return false
        }
        for i in 0..a.len() {
            if a[i].0 != b[i].0 {return false}
            if a[i].1 != b[i].1 {return false}
            if a[i].2 != b[i].2 {return false}
            if a[i].3 != b[i].3 {return false}
        }
        return true
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
