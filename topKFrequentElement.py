class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        freq_sorted = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        print(freq_sorted)
        most_freq = [key for key, value in freq_sorted[:k]]
        return most_freq
