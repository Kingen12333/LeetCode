#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        product_left = 1
        for i in range(len(nums)):
            res[i] *= product_left
            product_left *= nums[i]
        product_right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= product_right
            product_right *= nums[i]

        return res


            
        
# @lc code=end

