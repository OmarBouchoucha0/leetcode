class Solution:
   
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1
        for i in range(len(t)):
            if t[i] in seen:
                if seen[t[i]] == 0:
                    return False
                else:
                    seen[t[i]] -= 1
            else:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for i in range(len(strs)):
            found = False
            for j in range(len(anagrams)):
                if self.isAnagram(anagrams[j][0], strs[i]):
                    anagrams[j].append(strs[i])
                    found = True
                    pass
            if not found:
                anagrams.append([])
                anagrams[-1].append(strs[i])
        return anagrams

