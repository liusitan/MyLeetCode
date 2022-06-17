#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
from optparse import Option
from typing import List, Optional, Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def new(id:0,l:List[int]) ->ListNode:
    if id <len(l):
        return ListNode(l[id],new(id+1,l))
    else:
        return None
def displayLinkedList(head:ListNode)->str:
    if head:
        return str(head.val)+"," + displayLinkedList(head.next)
    else:
        return ""
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def getLength(head:Optional[ListNode])->int:
#             count = 0
#             while head:
#                 head = head.next
#                 count += 1
#             return count
#         def extract(head:Optional[ListNode],step_size:int)->Union[ListNode,ListNode,ListNode,ListNode]:
#             first_start=None
#             first_end = None
#             second_start = None
#             second_end = None
#             # dummy = ListNode(0,head)
#             m = step_size//2
#             first_start = head.next
#             cur = head
#             count = 0
#             if first_start:
#                 while cur.next and count <m:
#                     cur = cur.next
#                     count +=1
#                 first_end = cur
#             if cur:
#                 second_start = cur.next
#                 if second_start:
#                     while cur.next and count < step_size:
#                         cur = cur.next
#                         count+=1
#                     second_end = cur
#             first_end.next = None
#             return first_start,first_end,second_start,second_end
#         def merge(fs:Optional[ListNode],ss:Optional[ListNode])->Union[ListNode,ListNode]:
#             dummy = ListNode(0)
#             cur = dummy
#             # while fs or ss:
#             #     fv = float('inf')
#             #     sv = float('inf')
#             #     if fs:
#             #         fv = fs.val
#             #     if ss:
#             #         sv = ss.val
#             #     if fv >= sv:
#             #         cur.next = ss
#             #         cur = cur.next
#             #         ss = ss.next
#             #     else:
#             #         cur.next = fs
#             #         cur = cur.next
#             #         fs = fs.next
#             # cur.next = None
#             l = fs
#             r = ss
#             while(l and r):
#                 if l.val < r.val:
#                     cur.next, l = l, l.next
#                 else:
#                     cur.next, r = r, r.next
#                 cur = cur.next
            
#             cur.next = l if l is not None else r
#             while cur.next is not None: cur = cur.next
#             # return dummy.next,cur
#             return dummy.next,cur
                
#         l = getLength(head)
#         if l <= 1:
#             return head
#         step = 2
#         dummy = ListNode(0,head)
#         while step<= 2*l:
#             p = 0
#             cur = dummy
#             while( p < l):
#                 fs,fe,ss,se = extract(cur,step)
#                 if se:
#                     cur.next = se.next
#                     se.next = None
#                     s,e = merge(fs,ss)
#                     e.next = cur.next
#                     cur.next  = s
#                     cur = e
#                 p = p + step
#             step *= 2
#         return dummy.next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        
        def getSize(head):
            counter = 0
            while(head is not None):
                counter +=1
                head = head.next
            return counter
        
        def split(head, step):
            i = 1
            while (i < step and head):
                head = head.next
                i += 1
                
            if head is None: return None
            #disconnect
            temp, head.next = head.next, None
            return temp
        
        def merge(l, r, head):
            cur = head
            while(l and r):
                if l.val < r.val:
                    cur.next, l = l, l.next
                else:
                    cur.next, r = r, r.next
                cur = cur.next
            
            cur.next = l if l is not None else r
            while cur.next is not None: cur = cur.next
            return cur

        size = getSize(head)
        bs = 1
        dummy = ListNode(0)
        dummy.next = head
        l, r, tail = None, None, None
        while (bs < size):
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = split(l, bs)
                cur = split(r, bs)
                tail = merge(l, r, tail)
            bs <<= 1
        return dummy.next
s = Solution()
head = new(0,[4,2,1,3])
print(displayLinkedList(head))
head = s.sortList(head)
print(displayLinkedList(head))

# a = 1
# @lc code=end

