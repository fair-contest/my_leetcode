use std::collections::BinaryHeap;

use std::collections::BinaryHeap;

impl Solution {
    pub fn trim_mean(arr: Vec<i32>) -> f64 {
        let r = arr.len() / 20;
        let mut heap_min = BinaryHeap::with_capacity(r+1);
        let mut heap_max = BinaryHeap::with_capacity(r+1);
        let mut i = 0;
        let mut sum = 0;
        while i < 2 * r {
            heap_min.push(arr[i]);
            heap_max.push(-1 * arr[i+1]);
            i += 2;
        }
        sum = Solution::ex_heap(&mut heap_max, &mut heap_min, arr[i as usize]);
        i += 1;
        for j in 0..(r-1) {
            sum = Solution::ex_heap(&mut heap_max, &mut heap_min, sum);
        }
        while i < arr.len() {
            sum += Solution::ex_heap(&mut heap_max, &mut heap_min, arr[i]);
            i += 1;
        }
        sum as f64 / (arr.len() - r * 2) as f64
    }

    fn ex_heap(h_max: &mut BinaryHeap<i32>, h_min: &mut BinaryHeap<i32>, v: i32) -> i32 {
        h_min.push(v);
        h_max.push(-1 * h_min.pop().unwrap());
        h_max.pop().unwrap() * -1
    }
}
