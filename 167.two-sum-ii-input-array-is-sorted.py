#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(numbers)-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if(sum < target):
                left += 1
            elif(sum == target):
                return [left+1, right+1]
            else:
                right -= 1

        return []



    

        
# @lc code=end

