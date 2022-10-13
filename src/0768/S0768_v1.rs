impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let mut rec = vec![0; arr.len()+1];
        rec[0] = 0;
        let mut cur = arr[0];
        let mut p = 0;
        for i in 0..arr.len() {
            while arr[i] < rec[p] {p -= 1;}
            if arr[i] > cur {cur = arr[i];}
            p += 1;
            rec[p] = cur;
        }
        p as i32     
    }
}
