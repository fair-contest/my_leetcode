class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum(1 for w in words if re.compile(''.join(''.join(('(',i[0],''.join(('{1,',str(len(tuple(i[1]))))).replace('1,2','2'),'})')) for i in groupby(s))+'$').match(w))
