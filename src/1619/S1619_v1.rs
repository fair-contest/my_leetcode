impl Solution {
    pub fn trim_mean(arr: Vec<i32>) -> f64 {
        let r = arr.len() / 20;
        let mut heap_min = std::collections::BinaryHeap::with_capacity(r+1);
        let mut heap_max = std::collections::BinaryHeap::with_capacity(r+1);
        let mut i = 0;
        let mut tmp = 0;
        let mut sum = 0;
        while i < 2 * r {
            heap_min.push(arr[i]);
            heap_max.push(-1 * arr[i+1]);
            i += 2;
        }
        while i < arr.len() {
            heap_min.push(arr[i]);
            tmp = heap_min.pop().unwrap();
            heap_max.push(-1 * tmp);
            sum += heap_max.pop().unwrap() * -1;
            i += 1;
        }
        sum as f64 / (arr.len() - r * 2) as f64
    }
}
