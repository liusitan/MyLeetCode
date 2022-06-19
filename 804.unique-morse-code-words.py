#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        tmp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        m = {chr(i+ord('a')):v for i,v in enumerate(tmp)}
        s = set()
        for word in words:
            s.add( ''.join([m[i] for i in word]))
        return len(s)
# @lc code=end

