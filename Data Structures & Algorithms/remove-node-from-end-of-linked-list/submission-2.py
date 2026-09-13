# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        temp=head
        while temp!=None:
            temp=temp.next
            l+=1
        if l==1 and n==1:
            return None
        if l==1 and n!=0:
            return head
        dl=l-n
        if dl==0:
            return head.next
        temp=head
        l=0
        while temp!=None and l<dl-1:
           temp=temp.next
           l+=1
        
        if temp==None or temp.next==None:
            return head
        temp.next=temp.next.next
        return head