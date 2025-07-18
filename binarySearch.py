class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        upper = len(nums) - 1
        lower = 0
        i = 0
        while upper >= lower:
            i += 1
            middle = lower + (upper - lower) // 2
            print(upper, lower, middle)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                upper = middle - 1
            elif nums[middle] < target:
                lower = middle + 1
        return -1
