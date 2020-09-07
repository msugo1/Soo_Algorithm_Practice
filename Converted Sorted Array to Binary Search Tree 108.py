# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# first try
# the given list is sorted in ascending order (nums)
# pick out the middle value and call the function in recursion

# ex) nums = [1, 2, 7, 9, 10]
# mid = len(nums) // 2 = 2 (in this case)
# create a tree node with the mid index - node = TreeNode(nums[mid] = 7)
# node.left = mid value in a list from the start to mid - 1 (not including the current mid) /
# node.right = the same but from mid + 1 to the end
# like binary search

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bst(num_list):
            # base_case
            if len(nums) < 2:
                return TreeNode(nums[-1])

            # recursive_case
            mid = len(nums) // 2

            node = TreeNode(nums[mid])

            node.left = bst(nums[:mid])
            node.right = bst(nums[mid + 1:])

        ans = bst(nums)
        return ans

# result - time limit exceeded or maximum depth in recursion

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(nums[-1])

            # recursive_case
        mid = len(nums) // 2

        node = TreeNode(nums[mid])

        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

# weirdly, as soon as dfs got removed and the function executed in itself, the error had gone like magic
# why so?
# a mistake could be spotted with a help from stackover flow!
# I was just writing without consciousness on parameters. completely forgot that num_list was the one not nums lol
# so the list was not really decreasing throughout the whole process.

# answer from PAI
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

            # recursive_case
        mid = len(nums) // 2

        node = TreeNode(nums[mid])

        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node
# well base case can be just if not nums, return None then not only can a line be saved,
# but also creating a node in base cases doesn't need considering


