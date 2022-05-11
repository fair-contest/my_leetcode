// 我这个代码在Leetcode双100%达成，才收在这里，算法方面没可说， 因为很简单，就是广度优先遍历。
// https://leetcode.cn/problems/maximum-depth-of-binary-tree/solution/by-laughing-davincizbw-twoh/

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 1;
        let mut sav = Vec::new();
        if let Some(_root) = root {
            sav.push(Rc::clone(&_root));
        } else { return 0; }
        loop {
            let mut next = Vec::new();
            while let Some(node) = sav.pop() {
                if let Some(_left) = &node.borrow().left { next.push(Rc::clone(&_left)); }
                if let Some(_right) = &node.borrow().right { next.push(Rc::clone(&_right)); }
            }
            if next.is_empty() {
                break;
            } else {
                sav = next;
                res += 1;
            }
        }
        res
    }
}
