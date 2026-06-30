class Solution:
    def isDivisor(self, inp: str, target: str) -> bool:
        if len(inp) % len(target) != 0:
            return False
        i = 0
        while i < len(inp):
            if inp[i : i + len(target)] != target:
                return False
            i += len(target)
        return True

    def divisor(self, inp: str) -> list[str]:
        res = []
        if len(inp) == 1:
            return [inp]
        for i in range(1, len(inp)):
            for j in range(len(inp) - i):
                if self.isDivisor(inp, inp[j : j + i]):
                    res.append(inp[j : j + i])
        return res

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        div1 = self.divisor(str1)
        for div in div1:
            if self.isDivisor(str2, div) and len(div) > len(ans):
                ans = div
        return ans
