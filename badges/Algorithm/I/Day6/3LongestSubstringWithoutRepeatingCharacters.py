class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,m = 0,0,0
        d = {}    
        while j < len(s):
            if d.get(s[j])==None:
                d[s[j]]=j
                j+=1
                m = max(m, len(d.keys()))
            else:
                del d[s[i]]
                i+=1
        return m