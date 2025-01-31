#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        complement_dict = {}
        for idx, value in enumerate(nums):
            complement = target-value
            complement_index = complement_dict.get(value, None)

            if(complement_index != None):
                return [complement_index, idx]
            
            complement_dict[complement] = idx







# @lc code=end

