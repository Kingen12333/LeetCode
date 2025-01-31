#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    
        left,right = 0, len(height)-1

        left_max, right_max = height[left], height[right]

        res = 0
        while left < right:
            if left_max < right_max:
                left += 1
                h = height[left]
                left_max = max(left_max, h)
                res += left_max - h
            else:
                right -= 1
                h = height[right]
                right_max = max(right_max, h)
                res += right_max -h

        return res            
                
            
                

                


        
        

                
        




# @lc code=end

