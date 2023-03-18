from string import ascii_lowercase as alpha
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p)>len(s):
            return []

        counter={c:0 for c in alpha}
        res=[]
        l,r=0,len(p)-1

        for c in p:
            counter[c]-=1
        for i in range(r+1):
            counter[s[i]]+=1

        while r<len(s):
            if max(counter.values())==min(counter.values())==0:
                res.append(l)
            counter[s[l]]-=1
            l,r=l+1,r+1
            if r<len(s):
                counter[s[r]]+=1

        return res