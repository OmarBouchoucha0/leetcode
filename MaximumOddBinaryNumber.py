class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_of_1 = 0
        for c in s:
            if c == "1":
                count_of_1 += 1
        res = []
        for _ in range(count_of_1 - 1):
            res.append("1")
        for _ in range(len(s) - count_of_1):
            res.append("0")
        res.append("1")
        return "".join(res)
