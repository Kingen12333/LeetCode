#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        countS = {}
        countT = {}

        if (len(s) != len(t)):
            return False
    
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False

        return True


        
# @lc code=end

