class Solution:
    def topKFrequentFreq(self, nums: List[int], k: int) -> List[int]:
        res = [0 for _ in range(k)]
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        freq = [[] for _ in range(len(nums)+1)]
        for n,f in d.items():
            freq[f].append(n)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        heap = []
        for n,f in d.items():
            heapq.heappush(heap, (-f,n))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
