# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first=0
        n=0
        while(l1 is not None):
            first+= l1.val * (10 ** n)
            n+=1
            l1=l1.next
        
        second=0
        n=0
        while(l2 is not None):
            second+= l2.val * (10 ** n)
            n+=1
            l2=l2.next

        total=first+second
        
        node=ListNode(val=int(str(total)[0]), next=None)
        for i in (str(total)[1:]):
            node=ListNode(val=int(i), next=node)
        return node
        
