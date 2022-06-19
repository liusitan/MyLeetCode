#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from typing import Deque, List


class TreeNode:
    children: List
    isEnd: bool

    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
    
    
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        t = self.root
        for i in word:
            if not t.children[ord(i) - ord('a')]:
                t.children[ord(i) - ord('a')] = TreeNode()
            t = t.children[ord(i) - ord('a')]
        t.isEnd = True

    def search(self, word: str) -> bool:
        return self.match(self.root,word)
        return False
    def match (self,node:TreeNode, word)->bool:
        if not node:
            return False
        if not word:
            return node.isEnd
        else:
            if word[0]==".":
                for i in node.children:
                    if i and self.match(i,word[1:]):
                        return True
            else:
                return self.match(node.children[ord(word[0]) - ord('a')],word[1:])
                
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

