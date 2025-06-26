class Solution:
    def reverseWords(self, s: str) -> str:
        slow,fast=0,0
        res=""
        while fast < len(s):
            if s[fast]!=" ":
                fast+=1
            elif s[fast]==" ":
                res+=s[slow:fast][::-1]+" "
                fast+=1
                slow=fast
        res+=s[slow:][::-1]
        return res

#The easy one
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split(" ")])