# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            return max(left, right) + 1

# this is the basic structure
# now how I can calculate the height of left and rigth and the difference between them

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            if left - right > 1 or right - left > 1:
                return 100
            return max(left, right) + 1

# second try
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            if left - right > 1 or right - left > 1:
                return 100
            return max(left, right) + 1

        return dfs(root) != False

# fail - [1,2,2,3,null,null,3,4,null,null,4] - return True but should have been False
# why? I tracked it all down by writing the process down
# and when left 2 right 0 on the left and left 0 right 2 on the right both returns False
# so now addtion of False and False // noteworthy that boolean in python has their own value
# true = 1, false = 0
# so the last call of the recursion yields 0 as an answer which means dfs(root) != False gives true

# now give False + False an exception how?
"""
            if left - right > 1 or right - left > 1:
                return 100
            if left is False or right is False:
                return False
            return max(left, right) + 1
"""
# but it still returns true - why? dfs(root) - left: False, right: 1  1 - 0(False) return 2
# 2 != False
# well it was just because I mistyped here 'return 100' - as soon as I changed it to return False it worked

# answer from PAI (Python Algorithm Interview)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) != -1

# wow... to begin with, didn't even know 'abs' could have been used here instead in a complicated way
# (left - right > 1 or right - left > 1)

# secondly, instead of false another value is used with the conditions combined (left == -1, right == -1)
# possibly, it worked changing

#             if left - right > 1 or right - left > 1:
#                 return 100
#             if left is False or right is False:
#                 return False

# to just if left is False or right is False or abs(left-right) > 1

# lastly, not until I read the explanation, did I realise how amazing it was to set -1 as return (when the difference exceeds 1)
# because leaf nodes will always return 1 (what their children return - 0 - will yield 1 by max(left, right) + 1)
# and once either left or right becomes -1, the fact their counterpart is a left node can't make any difference
# (-1 -1 / or 1 - (-1) whichever comes to a total of 2 as with abs)
# I'm so gobsmacked. How could the author come up with this in the first place?.

# today's learning point
# 1. boolean in python has its own num value(False - 0, True - 1)
# 2. ensure if conditional sentences can be combined together
# 3. if specific values are returned in recursion, they can also be calculated in equations
# (like above left + right is possible, I didn't know this truth so couldn't get my head around the question quite a while,
# even after I came up with the basic structure of the recursion process)