# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:        
        while head!=None and head.val==val:head=head.next
        if head==None: return head

        node=head
        while node!=None:
            if node.next!=None and node.next.val==val:
                node.next=node.next.next
            else:
                node=node.next
        return head
