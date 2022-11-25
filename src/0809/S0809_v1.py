class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        #return sum(1 for i in words if re.compile("("+"{3,100})(".join((c+'?|'+c for c in i)) + "{3,100})$").match(s))
        return sum(1 for i in words if re.match("".join(('('+c+'|'+c+'{3,100})('+c+'(?='+c+'))?' for c in i)) + "$", s))
