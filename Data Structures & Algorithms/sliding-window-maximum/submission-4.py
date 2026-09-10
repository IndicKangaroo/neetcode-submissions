class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        prevmax = max(nums[:k])
        res.append(prevmax)

        for i in range(1, len(nums) - k + 1):
            new_num = nums[i + k - 1]

            if nums[i - 1] == prevmax:
                prevmax = max(nums[i:i + k])
            else:
                prevmax = max(prevmax, new_num)

            res.append(prevmax)

        return res