class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum(1 for i in words if re.compile("("+"{3,100})(".join((c+'?|'+c for c in i)) + "{3,100})$").match(s))
