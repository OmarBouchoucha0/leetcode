class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        if len(nums) < 2:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums) < 3:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            else:
                return -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        if nums[mid] == target:
            return mid
        elif mid == len(nums) - 1:
            right = mid - 1
            left = 0
        elif nums[-1] >= target >= nums[mid + 1]:
            left = mid + 1
            right = len(nums) - 1
        else:
            right = mid - 1
            left = 0

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
