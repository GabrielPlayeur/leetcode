# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None: return head
        lastHead,head,nextHead=None,head,head.next
        head.next=lastHead
        while nextHead!=None:
            lastHead,head,nextHead=head,nextHead,nextHead.next
            head.next=lastHead
        return head