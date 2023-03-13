from string import ascii_lowercase as alpha
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        counter={i:0 for i in alpha}
        for i in range(len(s1)):
            counter[s1[i]]+=1
            counter[s2[i]]-=1
        if self.checkAllZero(counter): return True
        for i in range(len(s1),len(s2)):            
            counter[s2[i]]-=1
            counter[s2[i-len(s1)]]+=1
            if self.checkAllZero(counter): return True
        return False
        
    def checkAllZero(self, counter: dict) -> bool:
        return max(counter.values())==0 and min(counter.values())==0