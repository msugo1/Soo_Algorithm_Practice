# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

# with heapq

# python offers nlargest in heapq
# it sorts elements from the largest to the nth largest in descending order
# how to use: heapq.nlargest(n (nth), list)
# return heapq.nlargest(n (nth), list)'s the last data

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = heapq.nlargest(k, nums)
        return data[len(data) - 1]

        # from Python Algorithm Interview
        # shortened to
        # return heapq.nlargest(k, nums)[-1]

        # from LeetCode
        # even return min(heapq.nlargest(k, nums) is possible

# by sorting the given list
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# I didn't understand what it meant at first
# but realised it just means it will be the one that's kth from the sorted list

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

        # from Python Algorithm Interview
        # shortened to
        # return sorted(nums, reverse=True)[k - 1]

# with heapify (from Python Algorithm Interview)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
# heapify is needed only one time without any other elements added to the list
# iterating heappop for len(list) - k times means the nth largest one is now the first element of the heap
# so, pop and return it simultaneously

# without heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # or list()

        # only min-hip exists
        # so reverse it by making all the values negative
        # then when returning, it will have another negative mark to get back to plus again.
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k - 1): # in the book, it's 'k' but I'm guessing k is a typo as pop removes even the answer
            heapq.heappop(heap)

        return -heapq.heappop(heap)
