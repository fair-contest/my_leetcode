impl Solution {
    pub fn three_equal_parts(arr: Vec<i32>) -> Vec<i32> {
        let alen = arr.len();
        let mut cnt = 0;
        let mut a1 = 0;
        for v in (0..alen) {
            if arr[v] == 1 {cnt += 1;a1 = v; break;}
        }
        for v in (a1+1..alen) {
            if arr[v] == 1 {cnt += 1;}
        }
        if cnt == 0 {return [0, alen as i32 - 1].to_vec()};
        let fail = vec![-1, -1];
        if cnt % 3 != 0 {return fail};
        for v in (0..alen) {
            if arr[v] == 1 {a1 = v; break;}
        }
        // let a1 = arr.iter().take_while(|&&x| x!=1).count();
        let mut a2 = 2 * cnt as usize / 3;
        let mut a3 = cnt as usize / 3;
        let mut cnt = 0 as usize;
        for v in (a1..alen).rev() {
            if arr[v] == 1 {
                cnt += 1;
                if (cnt == a3 as usize) {
                    a3 = v;
                    break;
                }
            }
        }
        let r = alen - a3;
        for v in (a1+r..a3) {
            if arr[v] == 1 {
                a2 = v;
                break;
            }
        }
        if a1+r > a2 || a2+r > a3 {return fail;}
        let mut i: usize = a1;
        let mut j: usize = a2;
        for v in (a3..alen) {
            if arr[v] != arr[i] || arr[v] != arr[j] {return fail;}
            i += 1;
            j += 1;
        }
        [i as i32 - 1, j as i32].to_vec()
    }
}
