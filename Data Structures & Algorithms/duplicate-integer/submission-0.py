class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = []
        for i in nums:
            if i in nums1:
                return True
            else:
                nums1.append(i)
        return False
         