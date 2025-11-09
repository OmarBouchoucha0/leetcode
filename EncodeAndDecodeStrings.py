class Solution:
    def encode(self, strs: List[str]) -> str:
        final = list()
        for string in strs:
            final.append(" " + string)
        return final

    def decode(self, s: str) -> List[str]:
        words = s.split()
        return words
