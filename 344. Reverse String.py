# https://leetcode.com/problems/reverse-string/

# 1) swap with two pointers
# Python enables users to swap two variables without temp only if it's done in the same line
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# by using for
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        for left_index in range(len(s) // 2):
            right_index = len(s) - 1 - left_index

            s[left_index], s[right_index] = s[right_index], s[left_index]

# 2) a Pythonic way
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

# or just list slicing like yesterday

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        s[:] = s[::-1]