class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        local_seq = 1
        max_seq = 0
        i = 0
        j = 1
        while i < len(nums):
            if nums[i] + 1 in unique_nums and nums[i] - 1 not in unique_nums:
                while nums[i] + j in unique_nums:
                    unique_nums.discard(nums[i] + j)
                    local_seq += 1
                    j += 1
            if local_seq > max_seq:
                max_seq = local_seq
            local_seq = 1
            i += 1
            j = 1
        return max_seq
