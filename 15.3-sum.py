#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        nums = sorted(nums)
        
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if (i > 0 and a == nums[i-1]):
                continue
        

            left = i+1
            right = len(nums)-1

            while left < right:
                sum = a + nums[left] + nums[right]
                if sum == 0:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return res
                


            


                


# @lc code=end

