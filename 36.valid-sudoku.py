#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_sets = [set() for i in range(9)]
        col_sets = [set() for i in range(9)]
        sub_box = [set() for i in range(9)]

        size = len(board)
        row = 0
        col = 0
        for row in range(size):
            for col in range(size):
                value = board[row][col]

                if(value != "."):
                    box_index = (row // 3)*3 + (col // 3)
                    is_valid = value not in (row_sets[row] | col_sets[col] | sub_box[box_index])
                    if(is_valid == False):
                        return False
                    row_sets[row].add(value)
                    col_sets[col].add(value)
                    sub_box[box_index].add(value)

        return True
# @lc code=end

