from math import inf
class Solution:
    def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L > R: return -inf
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid+1, R+1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums)-1)
    def maxSubArray(self, nums):
        max_so_far = -inf
        max_ending_here = 0

        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0  
        return max_so_far