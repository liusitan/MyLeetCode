#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local_name , domain_name = email.split("@")
            local_name  = re.sub('([.]|\+[\S]+)','',local_name)
            s.add(local_name + "@" + domain_name)
        return len(s)
s = Solution()
s.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])
# @lc code=end

