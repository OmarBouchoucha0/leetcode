class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        first_stone = 0
        first_index = 0
        second_stone = 0
        second_index = 0
        while len(stones) > 1:
            for i in range(len(stones)):
                if stones[i] > first_stone:
                    first_stone = stones[i]
                    first_index = i

            for i in range(len(stones)):
                if stones[i] > second_index and i != first_index:
                    second_stone = stones[i]
                    second_index = i
            if first_stone > second_stone:
                stones[first_index] = first_stone - second_stone
                stones.pop(second_index)
            elif second_stone > first_stone:
                stones[second_index] = second_stone - first_stone
                stones.pop(first_index)
            else:
                if first_index > second_index:
                    stones.pop(first_index)
                    stones.pop(second_index)
                else:
                    stones.pop(second_index)
                    stones.pop(first_index)
        if len(stones) == 1:
            return stones[0]
        return 0
