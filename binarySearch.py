class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        upper = len(nums)
        lower = 0
        while upper - lower > 0:
            middle = int((upper + lower) / 2)
            print(upper, lower, middle)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                upper = middle
            elif nums[middle] < target:
                lower = middle
        return -1
