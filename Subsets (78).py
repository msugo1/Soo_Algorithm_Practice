# https://leetcode.com/problems/subsets/
# first try
# seems similar to the previous questions with dfs and backtracking, so I'll try it with the same approach

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            res.append(path[:])

            if index >= len(nums):
                return

            for i in range(len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return res

# result - RecursionError: maximum recursion depth exceeded in comparison
# now time to fix the faulty parts

# second try
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def dfs(index, elements):
            for i in range(len(nums)):
                elements.append(nums[i])
                res.append(elements[:])
                dfs(i + 1, elements)
                elements.pop()

        dfs(0, [])
        return res

# changed a bit but can't come up with a clear base case... so recursion error keeps taking place

# The book(PAI - Python Algorithm Interview) dropped me a hint - create a tree first, what does it mean?
# third try
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            res.append(path[:])

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return res
# I FOUND WHAT HAD BEEN SO WRONG
# the range in a for iteration should have been from index to len(nums)... I forgot to set it that way and just put only
# range(len(nums)), which means the loop can't come to an end by iterating 0,1,2 / 0,1,2 forever
# even the base case isn't even needed for this question
# what a mistake I have to be careful of from the next time
