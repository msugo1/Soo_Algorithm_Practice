# first try
# thought simple recursion would do
# tree's sum starts from right so 'right and then middle then left' will be the order.
class Solution:
    value: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0

        right = self.bstToGst(root.right)
        self.value += root.val
        root.val = self.value
        left = self.bstToGst(root.left)

        return root
# got this in the first try. Glad I'm getting the hang of recursion more and more gradually

# this line can be even shorter
#        if not root:
#            return 0
# with just if root: (from python algorithm interview)
# so still a lot more to go for more precise and concise codes.
