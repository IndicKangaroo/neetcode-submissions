# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node,prev):
            if node==None:
                return prev
            nh=node.next
            node.next=prev
            return rev(nh,node)
        return rev(head,None)