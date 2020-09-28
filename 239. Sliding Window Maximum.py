# https://leetcode.com/problems/sliding-window-maximum/
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        i = 0

        while i + k <= len(nums):
            ans.append(max(nums[i:i + k]))
            i += 1

        return ans

# result - time limit exceeded (probably takes too much time for slicing the given list

# Brute Force from Python Algorithm Interview

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        ans = []

        for i in range(len(nums) - k + 1):
            ans.append(max(nums[i:i + k]))

        return ans

# I was thinking it might be over the time limit and the book was saying it passed the case submission at the time of 704m/s
# but it actually has the same time complexity as the previous one so time limit outstripped

# using queue and update maximum only if necessary

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        num_max = float('-inf')  # minimum in system
        ans = []

        queue = collections.deque()

        for i, v in enumerate(nums):
            queue.append(v)

            if i < k - 1:
                continue

            if queue[0] != num_max or num_max < v:
                num_max = max(num_max, max(queue))

            ans.append(num_max)
            queue.popleft()

        return ans

# result - wrong answer: when nums is [1, -1] and k is 1
# I guess maximum needs resetting... but when?

#             if queue[0] != num_max or num_max < v:
#                 num_max = max(float('-inf'), max(queue))
# added float('-inf') instead. so it passed [1, -1] but still not able to get away with the 49th input (such a long list)

# even solutions from Python Algorithm Interview shows Time Limit Exceeded

