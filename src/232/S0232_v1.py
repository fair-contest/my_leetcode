“”“
 个人原创的单栈队列实现思路
 这种单栈实现的性能要比常规的双栈解法速度快n倍， 因为避免了所有不必要的内存操作。
 思路上一个数组是模拟线性存储的数据栈， 另一个其实相当于单寄存器变量，作为记录头尾数据操作点的位置指针。
 
 纯Python解法, 没用到切片外的任何python内置函数
 
 这里比我在力扣上发布的题解多实现了类似clear效果的reset函数
 https://leetcode.cn/problems/implement-queue-using-stacks/solution/by-laughing-davincizbw-qyeo/
 
 ultra-high performance queue implementation
 The performance of this algorithm is n times faster than conventional double-stack solutions
 The main idea is to use pointers to record the location of the head and tail data operation points
 The time complexity of the operation is O(1)
”“”

class MyQueue:

    def __init__(self):
        self.queue = [0] * 100
        self.point = [0, 0]

    def push(self, x: int) -> None:
        self.queue[self.point[1]] = x
        self.point[1] += 1

    def pop(self) -> int:
        self.point[0] += 1;
        return self.queue[self.point[0] - 1]

    def peek(self) -> int:
        return self.queue[self.point[0]]

    def empty(self) -> bool:
        return self.point[0] == self.point[1]
      
    def reset(self):
        self.queue[0] = 0
        self.point = [0, 0]
        
        
