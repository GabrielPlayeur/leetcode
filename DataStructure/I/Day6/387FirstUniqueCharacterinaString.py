class Solution:
    def firstUniqChar(self, s):
        d,seen = {},set()
        for i,c in enumerate(s):
            if c not in seen:
                d[c] = i
                seen.add(c)
            elif d.get(c)!=None: del d[c]
        return min(d.values()) if d else -1