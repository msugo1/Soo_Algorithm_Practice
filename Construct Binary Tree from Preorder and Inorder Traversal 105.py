# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# the first element of the pre-order result (list) divides the in-order result (list) into two parts (left and right)
# it keeps going till no counterpart element is left
# divide and conquer

# datum point - p.o(pre-order from here, p.o)[0]
# node = T.N(p.o[0])
# in i.o(in-order): left - 0 ~ p.o[0] // right - p.o[0] + 1 ~ end
# no need to worry about indices for right parts of the tree because left will be carried out first recursively and
# when it's time to do the right, the first index of p.o will automatically be the first node of the node.right
# I was able to come up with the logic vaguely on my own but can't really implement codes so had to refer to the explanation in the book.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        preorder.pop(0)

        node.left = self.buildTree(preorder, inorder[:index])
        node.right = self.buildTree(preorder, inorder[index + 1:])

        return node

# answer from PAI
#         node = TreeNode(preorder[0])
#         index = inorder.index(preorder[0])
#         preorder.pop(0)
# these three lines can be shortened to
# index = inorder.index(preorder.pop(0))
# node = TreeNode(inorder[index])

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

        return node

