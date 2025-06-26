# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None: return head
        FakeHead=ListNode(0)
        FakeHead.next=head
        pre,cur=FakeHead,head
        while(cur!=None):
            while(cur.next!=None and cur.val==cur.next.val):
                cur=cur.next
            if(pre.next==cur):
                pre=pre.next
            else:
                pre.next=cur.next
            cur=cur.next
        return FakeHead.next