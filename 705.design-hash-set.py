#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
from typing import Deque


class MyHashSet:

    def __init__(self):
        self.l = [Deque() for i in range(8)]
        self.load = 0
        self.length = 8
    def add(self, key: int) -> None:
        if self.load >self.length//2:
            self.length *=2
            self.remap()
        loc = key %self.length
        if key not in self.l[loc]:
            self.load += 1
            self.l[loc].append(key)     
    def remap(self)->None:
        nl = [Deque() for i in range(self.length)]
        for l in self.l:
            while l:
                e = l.pop()
                nl[e%self.length].append(e)
        self.l = nl
    
    def remove(self, key: int) -> None:
        loc = key %self.length
        if key in self.l[loc]:
            self.l[loc].remove(key)
    def contains(self, key: int) -> bool:
        loc = key %self.length
        return key in self.l[loc]

mhs = MyHashSet()
mhs.add(9)
mhs.remove(19)
mhs.add(14)
mhs.remove(10)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

