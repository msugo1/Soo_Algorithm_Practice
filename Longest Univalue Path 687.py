# https://leetcode.com/problems/longest-univalue-path/

# first try
# see left and right each, set l and r longest for maximum as well as l, r value for regular updates
# current_node.val == left.val - l += 1 and l longest = max(l longest, l) - update longest as the biggest value between the two
# do the same for right, and sum both longest in the end and return

class Solution:
    r_longest = 0
    l_longest = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            r = 0
            l = 0

            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            if left.val is not None and right.val is not None and left != -1 and right != -1:

                if node.val == left.val:
                    l += 1
                    self.l_longest = max(self.l_longest, l)
                else:
                    l = 0

                if node.val == right.val:
                    r += 1
                    self.r_longest = max(self.r_longest, r)
                else:
                    r = 0

        dfs(root)
        return self.r_longest

# result: AttributeError - int object has no attribute val
# was going to carry out dfs first and then back tracking from leaf nodes but seems like the code above can't resolve the base

# second try : dfs is done in leaf
class Solution:
    left_longest = 0
    right_longest = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node):
            left = 0
            right = 0

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.left_longest = max(self.left_longest, left)
            self.right_longest = max(self.right_longest, right)
            return max(left, right)

        dfs(root)
        return self.left_longest + self.right_longest
# result: output 3 which was meant to be 2
# why? why does separating left and right yield a different result...
# 

# answer - third try with Python Algorithm Interview
class Solution:
    result = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node):
            left = 0
            right = 0

            if node is None:
                return 0

            # till the leaf nodes
            left = dfs(node.left)
            right = dfs(node.right)

            # increase 1 if current node.val equals its child node.val for both left and right
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # update max result
            self.result = max(self.result, right + left)
            # this is what I couldn't think of
            # why not left + right?
            # because parents node can't choose both left and right but only either of them. so max should be chosen
            """
                      4 (<-- A)
                4  (<-- B)
            4       4
        4               3
        
        on B both paths
        on A only either straight left or left then right (which is shorter)
            """
            return max(left, right)

        dfs(root)
        return self.result

#             if node.left and node.left.val == node.val:
#                 left += 1
#             else:
#                 left = 0
#             if node.right and node.right.val == node.val:
#                 right += 1
#             else:
#                 right = 0

# these lines can be shorten to
#             left += 1 if node.left and node.left.val == node.val else 0
#             right += 1if node.right and node.right.val == node.val else 0
# just two lines