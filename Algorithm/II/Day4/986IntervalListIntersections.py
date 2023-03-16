class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        n,m=len(firstList), len(secondList)
        pt1,pt2=0,0
        res=[]
        while pt1<n and pt2<m:
            A1,A2,B1,B2=firstList[pt1][0],firstList[pt1][1],secondList[pt2][0],secondList[pt2][1]
            if A1<=B1<=A2 or B1<=A1<=B2:
                res.append([max(A1,B1),min(A2,B2)])
            if A2<B2:
                pt1+=1
            else:
                pt2+=1
        return res