# https://leetcode.com/problems/assign-cookies/submissions/

# have a look at the one from the least to the most greedy (assume the list is already sorted in ascending order)
# when one can't be content at a certain point, it means the rest as well?
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if sum(s) > sum(g):
            return len(g)

        cookies = sum(s)
        contented = 0

        for need in g:
            if cookies >= need:
                cookies -= need
                contented += 1
            else:
                break

        return contented

# my first try:
# I thought, when s is [3], it can be separated into 1, and 2, then assigned to two children with 1, 2 greedy factor
# but it gave me a wrong answer with g = [1, 2, 3] and s = [3]
# so my first idea was proved incorrect

# cookies in s don't have to be identical it can be above

# my second try:
# result - runtime: 164ms(86.43%), memory usage: 15.8MB(6.50%)
# focus on what I've found out: "cookies in s don't have to be identical it can be above"
# set two indices each for g and s
# if s[j] (cookies) has a higher value than g[i] (a child's greed level), give +1 to content
# then push both to the next index
# or cookies < greed level, move only j in order to have a look at the amount of cookies on the next index
# iterate till either of the indices reach the length of either of the two given lists

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # the two lists are actually not sorted at all
        g.sort()
        s.sort()

        i = 0
        j = 0
        content = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1

        return content

# a solution from Python Algorithm Interview
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        # iterate till one can't be content
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

# seems like it can be solved even with Binary Search
# The book's solution's based on the bisect module
# (Today's homework: study bisect on the Internet)
