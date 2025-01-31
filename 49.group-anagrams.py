#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        group_map = {}
        
        for str in strs:
            count = [0]*26
            for char in str:
                count[ord(char)-ord("a")] += 1
            
            if(group_map.get(tuple(count)) == None):
                group_map[tuple(count)] = [str]
            else:
                group_map[tuple(count)].append(str)

        return [val for val in group_map.values()]

        #group_map = {}
#
        #for idx, str in enumerate(strs):
        #    sorted_str = "".join(sorted(str))
        #    if group_map.get(sorted_str) == None:
        #        group_map[sorted_str] = [str]
        #    else:
        #        group_map[sorted_str].append(str)
        #
        #result_list = []
        #for val in group_map.values():
        #    result_list.append(val)
#
        #return result_list
            

        

        
# @lc code=end

