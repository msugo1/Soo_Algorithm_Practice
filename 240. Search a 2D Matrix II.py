# https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/

"""
# a 2D Matrix is given, and search it for the target

conditions:

1. Integers in each row are sorted in ascending from left to right.
2. Integers in each column are sorted in ascending from top to bottom.

Initial logic
- each row is sorted in ascending order from left to right, so Binary Search would be perfect
- the exception for unnecessary cases would reduce the runtime
(see the first and last element of an matrix[i], and then count the row out if the target is not within their range)
- Binary Search only for those in accordance with the condition above
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][len(matrix[i]) - 1]:
                left = 0
                right = len(matrix[i]) - 1

                while left <= right:
                    mid = left + (right - left) // 2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                continue

        return False

# result - Runtime Error: list index out of range
# it gives an error with inputs like [], [[]] (the case of having no elements in the matrix)
# so added some exceptions to the first line and then finally worked.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][len(matrix[i]) - 1]:
                left = 0
                right = len(matrix[i]) - 1

                while left <= right:
                    mid = left + (right - left) // 2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                continue

        return False

# result - runtime: 40ms (62.26%), memory usage: 18.5MB (64.55%)
# Can I improve the speed up a bit? If so, how?

# solution from PAI

# not Binary Search but, firstly, pick out the last element of the first row and then plus 1 row if target's higher
# or minus 1 if target's lower or return if it's the target

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1

        return False

# result: around the same runtime and memory usage

# one line solution
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return any(target in row for row in matrix)

# brilliant
# today's new learning
# any(): if any elements in any( ) is true, it returns true
# all(): only if all the elements in all( ) are true, it returns true
