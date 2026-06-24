class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        mini = sorted_nums[-1]
        for i in range(len(sorted_nums) - k + 1):
            diff = sorted_nums[i + k - 1] - sorted_nums[i]
            if diff < mini:
                mini = diff
        return mini
