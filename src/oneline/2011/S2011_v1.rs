impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        operations.iter().fold(0, |x, y|if y.contains("+") {x + 1} else {x - 1})
        // operations.iter().map(|x|if x.contains("+") {1} else {-1}).sum()
    }
}
