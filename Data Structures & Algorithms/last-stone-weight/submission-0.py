class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort(reverse=True)
        while len(stones) > 1:
            a = stones.pop(0)
            b = stones.pop(0)

            if a != b:
                rem = a - b

                for i in range(len(stones)):
                    if stones[i] < rem:
                        stones.insert(i, rem)
                        break
                else:
                    stones.append(rem)

        return stones[0] if stones else 0