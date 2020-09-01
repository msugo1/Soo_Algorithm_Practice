# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# I decided to skip the last two graph questions that has to do with Dijkstra Algorithm for the time being
# because it is just over my head at the moment, but I'm sure I'll go back to the questions again near future

# hint: BFS - it is not possible to solve BFS with recursion, so iteration

# first try
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        depth = 0
        queue = collections.deque()

        queue.append(root)

        while queue:
            depth += 1
            node = queue.popleft()

            if node.left is not None:
                queue.append(node.left)
            elif node.right is not None:
                queue.append(node.left)

        return depth

# wrong - when an input is [0], it returns 2, which is supposed to be 1 instead

# second try
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        depth = 1
        queue = collections.deque()
        visited = []

        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left is not None:
                queue.append(node.left)
            elif node.right is not None:
                queue.append(node.left)

            visited.append(node)

        return len(visited) // 2 + 1
# mark those elements that were popped out of the queue visited(here append in another list) and then thought len(visited) // 2 + 1 would work
# like visited = [3, 9, 20, 15, 17]
# len(visited) // 2 = 2 and + 1 = 3

# third try with Python Algorithm Interview
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth = 0
        queue = collections.deque([root])

        while queue:
            depth += 1

            # iteration only up to len(queue) so it won't be messed up with child nodes (key point)
            # the main difference to the first try
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth