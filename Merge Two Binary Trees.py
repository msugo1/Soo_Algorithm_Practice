# https://leetcode.com/problems/merge-two-binary-trees/

# first try
# neither t1 nor t2 = None
# only t1 then return t1, only t2 then set t1 as t2 and then return t1
# if both, try to compile t2 to t1

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def dfs_and_combine(t1, t2):
            if not t1 and not t2:
                return None
            if not t2:
                return t1
            if not t1:
                return t1

            TreeN = t1.val + t2.val
            left = dfs_and_combine(t1.left, t2.left)
            right = dfs_and_combine(t1.right, t2.right)

        dfs_and_combine(t1, t2)
        return t1

# return [3, 4, 5, 5] whereas the answer is [3, 4, 5, 5, 4, null, 7]
# How come the code stops after 4 recursion only

# second try
# created a new node to make a new merged tree

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.right)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node

        if not t1:
            return t2
        if not t2:
            return t1
        if not t1 and not t2:
            return None

# return [3,6,5,12,7,7,7] wth
# found why - node.left = self.mergeTrees(t1.left, t2.right)
# I couldn't spot the typo here t2.right should have been t2.left in node.left

# today's learning point
# 1. it is not always correct to create dfs inside a function
# 2. typo and typo!!
# 3.
#         if not t1:
#             return t2
#         if not t2:
#             return t1
#         if not t1 and not t2:
#             return None
# this line can be shortened to just else: return t1 or t2

# answer in Python Algorithm Interview
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node

        else:
            return t1 or t2

# Runtime - quite random - from around 90 to around 160