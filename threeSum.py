class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = []
        j = 0
        k = 0
        for i in range(len(sorted_nums) - 2):
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
                    if [sorted_nums[i], sorted_nums[j], sorted_nums[k]] not in ans:
                        ans.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                else:
                    if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] > 0:
                        k -= 1
                    if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] < 0:
                        j += 1
        return ans
