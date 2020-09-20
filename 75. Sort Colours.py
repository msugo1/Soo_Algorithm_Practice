# https://leetcode.com/problems/sort-colors/

# improvement of quick sort
# into three parts: below pivot, pivot, and above pivot

# pseudo-code in wekipidia

"""
def three-way- partition(A: array of values, mid: value)
    i = 0
    j = 0
    k = size of A

    while j < k:
        if A[j] < mid:
            swap A[i] and A[j]
            i += 1
            j += 1
        else if A[j] > mid:
            k -= 1
            swap A[j] and A[k]
        else:
            j += 1
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0  # i
        white = 0  # j
        blue = len(nums)  # size of A

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1

