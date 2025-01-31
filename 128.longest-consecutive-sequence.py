#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_set = set(nums)

        biggest_count = 0
        for val in num_set:
            if val+1 not in num_set:
                count = 1
                cur_val = val
                while cur_val-1 in num_set:
                    count += 1
                    cur_val -= 1
                if count > biggest_count:
                    biggest_count = count

        return biggest_count


            

# @lc code=end

