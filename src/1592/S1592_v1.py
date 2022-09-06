class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space = len(text) - sum(len(word) for word in words)
        if len(words) == 1:
            return words[0] + ' ' * space
        gap = space // (len(words) - 1)
        remaider = space % (len(words) - 1)
        res = ""
        for word in words[:(len(words) - 1)]:
            res += word + ' ' * gap
        return (res + words[-1] + ' ' * remaider) if remaider > 0 else res + words[-1]
 
