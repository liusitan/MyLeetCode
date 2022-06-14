#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def createLinkedList(arr):
    sentinel = ListNode(0)
    s = sentinel
    for i in arr:
        s.next = ListNode(i)
        s = s.next
    return sentinel.next
def printLinkedList(h:ListNode):
    res = []
    while h:
        res.append(h.val)
        h = h.next
    print(res)
#  * -> * -> * -> * -> * 
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        if(slow.next == None):
            return
        while(fast.next!=None and fast.next.next!=None):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                break
       
        def reverseList(head: Optional[ListNode]) ->  Optional[ListNode]:
            cur = head
            prev = None
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        middle = slow
        nextMiddle = slow.next
        slow.next = None
        tail = reverseList(nextMiddle)
        
        while tail: 
            headnext = head.next
            head.next = tail
            tailnext = tail.next
            tail.next = headnext
            tail = tailnext
            head = headnext
s = Solution()
l = createLinkedList([1,2,3,4])
s.reorderList(l)
printLinkedList(l)
# @lc code=end

