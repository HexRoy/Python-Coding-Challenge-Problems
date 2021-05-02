# Problem
# =====================================================================================================================
# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost
# column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal
# starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
#
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
#
#
#
# Example 1:
#
#
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# Example 2:
#
# Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100


# Solution
# ====================================================================================================================

# Solution ~ 80 ms,
class Solution:
    def diagonalSort(self, mat):
        height, width = len(mat), len(mat[0])
        blank_mat = [[0 for i in range(width)] for j in range(height)]

        diagonals_sorted = self.sort_diagonals(mat)
        unpacked_diagonals = self.repopulate_mat(diagonals_sorted, blank_mat)
        return unpacked_diagonals

    def sort_diagonals(self, mat):
        # Start at (0,0), (0,1), ....  (0,len(mat[0]))
        # Start again at (1,0), (2,0), .... (len(mat), 0)
        # Add all sorted sublists into array to be passed into repopulate mat
        packed_diagonals = []
        for i in range(len(mat[0])):
            height = 0
            width = i
            temp = []
            while height < len(mat) and width < len(mat[0]):
                temp.append(mat[height][width])
                height += 1
                width += 1
            packed_diagonals.append(sorted(temp))

        for j in range(1, len(mat)):
            height = j
            width = 0
            temp = []
            while height < len(mat) and width < len(mat[0]):
                temp.append(mat[height][width])
                height += 1
                width += 1
            packed_diagonals.append(sorted(temp))

        return packed_diagonals

    def repopulate_mat(self, sorted_packed_mat, blank_mat):
        # Does the reverse of sort_diagonals and uppacks each sublist into the blank mat
        for i in range(len(blank_mat[0])):
            height = 0
            width = i
            for num in sorted_packed_mat[i]:
                blank_mat[height][width] = num
                height += 1
                width += 1

        height_iter = 0
        for j in range(len(blank_mat[0]), len(sorted_packed_mat)):
            height = 1 + height_iter
            width = 0
            temp = []
            for num in sorted_packed_mat[j]:
                blank_mat[height][width] = num
                height += 1
                width += 1
            height_iter += 1
        return blank_mat

    # Input
# =====================================================================================================================
test = Solution()
print(test.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
