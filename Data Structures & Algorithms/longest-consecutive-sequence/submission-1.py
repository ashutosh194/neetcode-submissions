class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        list_hash = defaultdict(int)

        for i in range(n):
            list_hash[nums[i]] += 1
        
        max_seq_len = 0
        curr_seq_len = 0

        for i in range(-1000,1001,1):
            if list_hash[i] == 0:
                max_seq_len = max(max_seq_len,curr_seq_len)
                curr_seq_len = 0
                continue
            curr_seq_len += 1
        

        return max(max_seq_len,curr_seq_len)






        