class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        low = 0
        high = n-1 
        while low < high :
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low+1,high+1]
            if sum > target:
                high = high-1
            else:
                low = low+1
        return [-1,-1]
        

        