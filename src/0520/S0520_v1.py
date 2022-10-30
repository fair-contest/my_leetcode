class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.istitle() or word.isupper() or word.islower()
