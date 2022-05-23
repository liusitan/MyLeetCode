#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
'''
This code is correct running the testcases, but not work on leetcode platform
Basically, we represent a string as a series of node connected 
by edges , each edge represents a character in the string. 
if there is string, we denote the ending node's property isEnd as true.
In other word,if the node's isEnd is not true, it means the path from the root
node to this node is a substring of some key. 

'''
# @lc code=start
from typing import List


class TrieNode: 
    children:List = {}
    isEnd = False
    def __init__(self):
        self.children:List = {}
        self.isEnd = False
    def setEnd(self):
        self.isEnd = True
    def insert(self,a):
        self.children[a] = TrieNode()
        return self.children[a]
    def get(self,a):
        if a in self.children:      
            return self.children[a]
        return None
class Trie:
    root:TrieNode = TrieNode()
    def __init__(self):
        return None

    def insert(self, word: str) -> None:
        traverse = self.root
        for c in word:
            if(not traverse.get(c)):
                traverse.insert(c)
            traverse = traverse.get(c)
        traverse.setEnd()
        return 

    def search(self, word: str) -> bool:
        traverse:TrieNode = self.root
        for i in word:
            traverse = traverse.get(i)
            if not traverse:
                break
        
        return True if traverse.isEnd else False

    def startsWith(self, prefix: str) -> bool:
        traverse:TrieNode = self.root
        for i in prefix:
            traverse = traverse.get(i)
            if not traverse:
                return False
        return True

# Your Trie object will be instantiated and called as such:
word = "apple"
prefix = "app"
obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
param_3 = obj.startsWith("a")
print(param_3)
# @lc code=end

