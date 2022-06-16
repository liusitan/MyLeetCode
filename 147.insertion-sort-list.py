#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(float('-inf'),head)
        def insert(sentinel,node):
            prev = sentinel
            cur = sentinel.next
            while cur and cur.val < node.val:
                prev = cur
                cur = cur.next
            node.next = prev.next
            prev.next = node
        # prev = sentinel
        cur = head.next
        head.next =None
        while cur:
            next = cur.next
            cur.next = None
            insert(sentinel,cur)
            cur = next
        return sentinel.next
# @lc code=end

