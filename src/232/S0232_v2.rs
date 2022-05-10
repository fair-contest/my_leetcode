// v1版本基础上改成vector array的解法
struct MyQueue {
    queue: Vec<i32>,
    point: [usize; 2],
}

impl MyQueue {

    fn new() -> Self {
        Self {
            queue: vec![],
            point: [0, 0],
        }
    }

    fn push(&mut self, x: i32) {
        self.queue.push(x);
        self.point[1] += 1;
    }

    fn pop(&mut self) -> i32 {
        self.point[0] += 1;
        self.queue[self.point[0] - 1]
    }

    fn peek(&self) -> i32 {
        self.queue[self.point[0]]
    }

    fn empty(&self) -> bool {
        self.point[0] == self.point[1]
    }
}
