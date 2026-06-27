class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max = 0
        local_max = 0
        for i in range(len(nums)):
            local_max += nums[i]
            if i == len(nums) - 1 or nums[i] >= nums[i + 1]:
                if local_max > max:
                    max = local_max
                local_max = 0
        return max
