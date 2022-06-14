#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
i = a + r * c + offset
2i = a + r2 *c + offset

slow = head 
fast = head
while(fast!=None and fast.next !=None and slow!=fast):
this is incorrect because they are nitially the same
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head
        while(fast!=None and fast.next !=None):
            fast = fast.next.next
            slow = slow.next
            if(slow == fast):
                break
        if(fast == None or fast.next ==None):
            return None
        slow1 = head
        while(slow1!=slow):
            slow = slow.next
            slow1 = slow1.next
        return slow
            
# @lc code=end

