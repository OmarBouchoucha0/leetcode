class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        seen[target - nums[0]] = 0
        for i in range(1, len(nums)):
            if nums[i] in seen:
                return [seen[nums[i]], i]
            seen[target - nums[i]] = i
