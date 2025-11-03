class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = dict()
        for char in s1:
            if char in s1_dict:
                s1_dict[char] += 1
            else:
                s1_dict[char] = 1
        s2_dict = dict()
        for i in range(len(s1)):
            if s2[i] in s2_dict:
                s2_dict[s2[i]] += 1 
            else:
                s2_dict[s2[i]] = 1
        start = 0
        finish = len(s1)-1
        while finish < len(s2):
            if s1_dict == s2_dict:
                return True
            s2_dict[s2[start]] -= 1
            if s2_dict[s2[start]] == 0:
                s2_dict.pop(s2[start])
            start += 1
            finish += 1
            if finish >= len(s2):
                break
            if s2[finish] in s2_dict:
                s2_dict[s2[finish]] += 1
            else:
                s2_dict[s2[finish]] = 1
        return False



