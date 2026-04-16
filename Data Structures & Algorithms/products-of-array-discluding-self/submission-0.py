class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [0] * len(nums)
        n = len(nums)
        print(nums)
        for i in range(1,n):
            left[i] = nums[i-1] * left[i-1]
        for j in range (n-2,-1,-1):
            right[j] = nums[j+1] * right[j+1]
        for i in range(n):
            res[i] = left[i] * right[i]

        return res

        