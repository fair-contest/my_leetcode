impl Solution {
    pub fn mincost_to_hire_workers(quality: Vec<i32>, wage: Vec<i32>, k: i32) -> f64 {
        let mut res = f64::MAX;
        let mut qw = quality.into_iter().zip(wage.into_iter()).collect::<Vec<_>>();
        qw.sort_by_cached_key(|x:&(i32, i32)| ((x.1 as f64 / x.0 as f64) * 100000 as f64) as i64); // 因为rust的sort_by_key没实现直接比较f64， 所以采用处理后的整数比较
        let mut quality_sum = 0;
        let mut heap = std::collections::BinaryHeap::new();
        for i in 0..k-1 {quality_sum += qw[i as usize].0; heap.push(qw[i as usize].0);}
        for i in k-1..qw.len() as i32 {
            quality_sum += qw[i as usize].0;
            heap.push(qw[i as usize].0);
            let tmp = (qw[i as usize].1 as f64 / qw[i as usize].0 as f64) * quality_sum as f64;
            res = if res > tmp { tmp } else { res };
            quality_sum += -1 * (heap.pop().unwrap_or(0));
        }
        res
    }
}
