from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            list1 = str(l1.val) + list1
        list2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            list2 = str(l2.val) + list2
        answer = str(int(list1) + int(list2))
        l3 = ListNode(0)
        result = l3
        while answer:
            result.next = ListNode(int(answer[-1]))
            result = result.next
            answer = answer[:-1]
        return l3.next