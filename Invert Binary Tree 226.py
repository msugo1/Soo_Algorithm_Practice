# https://leetcode.com/problems/invert-binary-tree/

# It has been done for myself, for the first time in a while.
# To deep down the leaf nodes, and changes left and right from there.
import collections


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            # base_case (I wrote the latter condition at first because I thought only nodes with not None could be swapped)
            if not node or (not node.left and not node.right):
                return

            # define child nodes
            left = dfs(node.left)
            right = dfs(node.right)

            # and swap them // python doesn't necessarily require 'temp' as a bridge like Java
            node.left, node.right = node.right, node.left

        # activate dfs
        dfs(root)
        # then return inverted binary tree
        return root

# then realised that even if child nodes are None, it won't pose any errors with just two Nones swapped
# so if not node or (not node.left and not node.right) can just be if not node:

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return

            left = dfs(node.left)
            right = dfs(node.right)

            node.left, node.right = node.right, node.left

        # activate dfs
        dfs(root)
        # then return inverted binary tree
        return root

# Runtime: varies from 28 to 44 (don't know why this much fluctuation happens) - 60 ~ 80%
# Memory: 54.86%

# another solution in Python Algorithm Interview - this can be solved just within few lines
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
       if root:
           root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
           return root
       # None can be left out because a dynamic language like Python assigns of their own accord None
       #return None

# Let's try iterative BFS and DFS as well
# first of all, BFS with queue

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # queue = collections.deque()
        # queue.append(root)

        queue = collections.deque([root])

        while queue:
            visited = queue.popleft()

            # if visited added
            if visited:
                queue.append(visited.left)
                queue.append(visited.right)

                visited.left, visited.right = visited.right, visited.left

        return root

# result: AttributeError: 'NoneType' object has no attribute 'left'
# visited can be None so add 'if visited'
# Runtime and Memory Usage are quite similar
# collections.deque([root]) saves a line rather than write queue = collections.deque(), queue.append(root) separately

# then DFS
# everything else is the same but only queue.popleft() to queue.pop() because iterative DFS runs with stack



