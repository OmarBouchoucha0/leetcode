class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for i in range(len(temperatures) - 1):
            days = 1
            while temperatures[i] >= temperatures[i + days]:
                days += 1
                if days + i == len(temperatures):
                    days = 0
                    break
            answer.append(days)
        answer.append(0)
        return answer
