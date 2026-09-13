# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        head=res
        if list1==None and list2==None:
            return None
        while list1!=None and list2!=None:
            if list1.val>=list2.val:
                res.val=list2.val
                list2=list2.next
            else:
                res.val=list1.val
                list1=list1.next
            res.next=ListNode()
            res=res.next
        if list1==None:
            res.val=list2.val
            res.next=list2.next
        else:
            res.val=list1.val
            res.next=list1.next
        return head
        