# https://leetcode.com/problems/range-sum-of-bst/

# brute force (comparing all the values on the nodes and add if they within the range but it would take too much time
# guess the time complexity would be O(the number of nodes)
# one of the attributes of Binary Search Tree would probably be able to save some time
# left - node - right
# all of the left nodes are supposed to have lower values than node.val
# all of the right nodes are supposed to have higher values than node.val
# so probably no need to search further to the left or right if the values are out of range

class Solution:
    val: int = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root:
            if root.val < L:
                left = self.rangeSumBST(root.right, L, R)
            elif root.val > R:
                right = self.rangeSumBST(root.left, L, R)
            else:
                self.val += root.val
                left = self.rangeSumBST(root.left, L, R)
                right = self.rangeSumBST(root.right, L, R)

            return self.val
# Result - Runtime: 77.06% and Memory Usage: 58.57%

# answer from Python Algorithm interview
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if not node:
                return 0

            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
# more concise and much faster - Runtime: 220 m/s and it depends but more memory efficient
# 'return node.val + dfs(node.left) + dfs(node.right)'
# this part was particularly sensational because, first of all, I couldn't think of this concise line
# secondly, this line (if not node return 0) lets each node return integers as well as return sums at each stage
# which means set 'val' as a class variable isn't really required in the first place
# lastly, a lot faster in terms of speed

# second with iterative DFS
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        val_sum = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                if node.val < L:
                    stack.append(node.right)
                elif node.val > R:
                    stack.append(node.left)
                else:  # L <= node.val <= R
                    val_sum += node.val
                    stack.append(node.right)
                    stack.append(node.left)
        return val_sum
# result - runtime: 228ms 89.39% memory usage: 13.30%

# iterative solution from the book
# key point - only put valid nodes L < node.val append(node.left) / node.val < R append(node.right)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        val_sum, stack = 0, [root]

        while stack:
            node = stack.pop()

            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    val_sum += node.val

        return val_sum
