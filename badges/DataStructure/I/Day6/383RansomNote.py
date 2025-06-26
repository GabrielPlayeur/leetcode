from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magC,ranC = Counter(magazine),Counter(ransomNote)
        for k,v in ranC.items():
            if magC.get(k)==None or magC.get(k)<v: return False
        return True