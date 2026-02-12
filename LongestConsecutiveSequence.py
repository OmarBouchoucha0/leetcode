class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = []
        set_start = []
        for i in range(len(nums)):
            set_start.append([nums[i]])
            for j in range(len(nums)):
                if nums[j] == nums[i] - 1:
                    set_start.pop()
                    break
        seq = set()
        for i in range(len(set_start)):
            curr = set_start[i]
            seq.add(curr)
            for j in range(len(nums)):
                if nums[j] == curr + 1:
                    curr = nums[j]
                    seq.add(curr)
            result.append(len(seq))
        return max(result)
