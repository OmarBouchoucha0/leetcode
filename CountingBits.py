class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            for c in f"{i:b}":
                if c == "1":
                    count += 1
            res.append(count)
        return res
