# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        d = {}
        temp = head
        n = 0

        while temp:
            d[n] = temp
            n += 1
            temp = temp.next

        left = 0
        right = n - 1
        temp = head

        while left < right:
            temp.next = d[right]
            temp = temp.next
            right -= 1

            temp.next = d[left + 1]
            temp = temp.next
            left += 1

        temp.next = None