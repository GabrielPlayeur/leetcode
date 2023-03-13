# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None: return head
        node=head
        while node!=None:
            while node.next!=None and node.next.val==node.val:
                node.next=node.next.next            
            node=node.next
        return head