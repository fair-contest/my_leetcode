class Solution {
    public boolean checkIfPangram(String sentence) {
        return sentence.chars().reduce(67108863, (x, y) -> x & ~(1 << (y - 97))) == 0;
        // 也可以用下面的思路实现，从一个包含26个各异字母的字符串里删除遍历到的字符，如最后为空串，则返回真，但明显不如上面这么写。
        // return Stream.of(sentence.split("")).reduce("abcdefghijklmnopqrstuvwxyz", (x, y) -> x.replace(y, "")).isEmpty();
    }
}
