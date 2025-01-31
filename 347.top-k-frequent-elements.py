#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    from collections import Counter
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        occurance_count = Counter(nums)

        possible_distinct_values = max(occurance_count.values())
        freq = [[] for _ in range(possible_distinct_values + 1)]
        for number, count in occurance_count.items():
            freq[count-1].append(number)

        res = []
        for i in range(possible_distinct_values, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return []




# @lc code=end

