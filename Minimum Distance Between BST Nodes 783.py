# initial thought
# only consider node.val and node.right/left.val for the differences
# because left values of any nodes in BST should be lower than the nodes and right values are higher.

# tried to come up with recursive solutions but failed
# so, moved onto iterative ones

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min_diff = inf

    def minDiffInBST(self, root: TreeNode) -> int:

        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)

                if node.left:
                    left_diff = node.val - node.left.val
                else:
                    left_diff = inf

                if node.right:
                    right_diff = abs(node.right.val) - node.val
                else:
                    right_diff = inf

            self.min_diff = min(self.min_diff, left_diff, right_diff)

        return self.min_diff

# here stumbled upon this exception against my initial thought
# [90,69,null,49,89,null,52,null,null,null,null]

#               90
#
#           69      None
#
#       49      89
#
#   None    52

# 90 - root, 89 - root.left.right
# gap: 1

# what if I could get max from left and min from right and then see the difference between them and the node.val

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min_diff = inf
    max_value = -inf
    min_value = inf

    def minDiffInBST(self, root: TreeNode) -> int:

        def max_left(node):
            if node:
                self.max_value = max(self.max_value, node.val)

                left = max_left(node.left)
                right = max_left(node.right)

            return self.max_value

        def min_right(node):
            if node:
                self.min_value = min(self.min_value, node.val)

                left = min_right(node.left)
                right = min_right(node.right)

            return self.min_value

        if root:
            left = self.minDiffInBST(root.left)
            right = self.minDiffInBST(root.right)

            self.min_diff = min(self.min_diff, abs(root.val - max_left(root.left)),
                                abs(min_right(root.right) - root.val))

        return self.min_diff

# Wrong answer - input: [69,3,72,null,61,null,null,47,null,null,null] / output: 8 / expected: 3
# hint (from Python Algorithm Interview) - in order search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min_diff = inf

    def minDiffInBST(self, root: TreeNode) -> int:

        ###################################

        def max_left(node):
            left_max = -inf
            if not node:
                return left_max

            if not node.right:
                left_max = node.val
                return left_max

            right = max_left(node.right)

        ###################################

        def min_right(node):
            right_min = inf
            if not node:
                return right_min

            if not node.left:
                right_min = node.val
                return right_min

            left = min_right(node.left)

        ###################################

        if not root.left and root.right:
            return root.val

        self.min_diff = min(self.min_diff, root.val - max_left(root.left), min_right(root.right) - root.val)

        left = self.minDiffInBST(root.left)
        right = self.minDiffInBST(root.right)

        return self.min_diff

# result - TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'
# already spent like 2 hours.. I might as well come back tomorrow

# 10 Sep
# a first go
# again TypeError


