use std::collections::HashMap;

impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n > 4275 {return 0.99999;}
        let v: i32 = (n + 24) / 25;
        let mut cache = HashMap::new();
        Solution::dfs(v, v, &mut cache)
    }

    fn dfs(a: i32, b: i32, hash: &mut HashMap<(i32, i32), f64>) -> f64 {
        if a <= 0 && b <= 0 {return 0.5;}
        else if a <= 0 {return 1.0;}
        else if b <= 0 {return 0.0;}
        match hash.get(&(a, b)) {
            Some(val) => return *val,
            None => {
                let val = 0.25 * (Solution::dfs(a-4, b, hash) + Solution::dfs(a-3, b-1, hash) + Solution::dfs(a-2, b-2, hash) + Solution::dfs(a-1, b-3, hash));
                hash.insert((a, b), val);
                return val;
            }
        }
    }
}
