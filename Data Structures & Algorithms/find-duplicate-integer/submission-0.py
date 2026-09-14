class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    # Phase 1: detect the cycle
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: find the cycle entry (= the duplicate)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
  