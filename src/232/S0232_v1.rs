// 个人原创的单栈队列实现思路
// 这种单栈实现的性能要比常规的双栈解法速度快n倍， 因为避免了所有不必要的内存操作。
// 思路上一个数组是模拟线性存储的数据栈， 另一个其实相当于单寄存器变量，作为记录头尾数据操作点的位置指针。
// 这里比我在力扣上发布的题解多实现了类似clear效果的reset函数
// https://leetcode.cn/problems/implement-queue-using-stacks/solution/by-laughing-davincizbw-qyeo/
// ultra-high performance queue implementation
// The performance of this algorithm is n times faster than conventional double-stack solutions
// The main idea is to use pointers to record the location of the head and tail data operation points
// The time complexity of the operation is O(1)

struct MyQueue {
    queue: [i32; 100],
    point: [usize; 2],
}

impl MyQueue {

    fn new() -> Self {
        Self {
            queue: [0; 100],
            point: [0, 0],
        }
    }

    fn push(&mut self, x: i32) {
        self.queue[self.point[1]] = x;
        self.point[1] += 1;

    fn pop(&mut self) -> i32 {
        self.point[0] += 1;
        self.queue[self.point[0] - 1]
    }

    fn peek(&self) -> i32 {
        self.queue[self.point[0]]
    }

    fn is_empty(&self) -> bool {
        self.point[0] == self.point[1]
    }
    
    fn reset(&self) {
        self.point = [0, 0];
        self.queue[self.point[0]] = 0
    }
}
