from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict1, dict2 = Counter(nums1), Counter(nums2)
        res = []
        for k in dict1.keys() if len(dict1.keys())<len(dict2.keys()) else dict2.keys():
            v1,v2 = dict1.get(k),dict2.get(k) 
            if v1 != None and v2 != None:
                res.extend([k]*min(v1,v2)) 
        return res