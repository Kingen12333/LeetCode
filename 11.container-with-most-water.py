#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1

        max = 0
        while left < right:
            area = min(height[left], height[right]) * (right-left)
            if area > max:
                max = area
            if(height[left] <= height[right]):
                left += 1
            else:
                right -= 1

        return max

# @lc code=end

