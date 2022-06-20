#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split(' ')
        words2 = s2.split(' ')
        ss1 = set(words1)
        ss2 = set(words2)
        m1  ={}
        m2 ={}
        res = []
        for i in words1:
            m1[i] = m1.get(i,0)+ 1
        for i in words2:
            m2[i] = m2.get(i,0) + 1
        for k,v in m1.items():
            if v == 1 and k not in ss2:
                res.append(k)
        for k,v in m2.items():
            if v ==1 and k not in ss1:
                res.append(k)
        return res
                       
# @lc code=end

