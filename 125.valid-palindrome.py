#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters in a case-insensitive manner
            if s[left].lower() != s[right].lower():
                return False

            # Move pointers closer
            left += 1
            right -= 1

        return True

    


# @lc code=end

