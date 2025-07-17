class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            x = i + 1
            y = len(nums) - 1
            while x < y:
                if nums[x] + nums[y] == -nums[i]:
                    answer.append([nums[i], nums[x], nums[y]])
                    break
                elif nums[x] + nums[y] < nums[i]:
                    x += 1
                elif nums[x] + nums[y] > nums[i]:
                    y -= 1
        return answer
