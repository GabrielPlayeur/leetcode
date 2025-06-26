# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow,fast=head,head
        for _ in range(n): fast = fast.next
        if fast==None:
            head=head.next
            return head
        while fast.next != None:
            slow,fast=slow.next,fast.next
        slow.next = slow.next.next
        return head