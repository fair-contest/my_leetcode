class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        # python3下面的位运算写法没有上面的效率好和简洁
        # return reduce(lambda x, y: x & ~(1 << (ord(y) - 97)), sentence, 67108863) == 0
