class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = 0
        n2 = 0

        head1 = l1
        head2 = l2

        # Find lengths
        while l1:
            n1 += 1
            l1 = l1.next

        while l2:
            n2 += 1
            l2 = l2.next

        if n2 > n1:
            head1, head2 = head2, head1
        l1 = head1
        l2 = head2

        carry = 0

        while l1:
            a = l1.val

            if l2:
                b = l2.val
            else:
                b = 0

            s = a + b + carry

            l1.val = s % 10
            carry = s // 10

            l1 = l1.next

            if l2:
                l2 = l2.next
        if carry:
            temp = head1
            while temp.next:
                temp = temp.next

            temp.next = ListNode(carry)

        return head1