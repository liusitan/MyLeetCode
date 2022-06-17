#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import Deque, List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = Deque()
        for i in tokens:
            if i == "+":
                o1 = s.pop()
                o2 = s.pop()
                s.append(o2+o1)

            elif i == "*":
                o1 = s.pop()
                o2 = s.pop()
                s.append(o2*o1)

            elif i == "-":
                o1 = s.pop()
                o2 = s.pop()  
                s.append(o2-o1)
          
            elif i == "/":
                o1 = s.pop()
                o2 = s.pop()
                s.append(int(o2/o1))
            else:
                s.append(int(i))
            # print(s)
        return s.pop()
s = Solution()
s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
# @lc code=end

