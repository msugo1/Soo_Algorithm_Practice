# https://leetcode.com/problems/maximum-subarray/

"""
ex)
nums = [-2,1,-3,4,-1,2,1,-5,4]
output: 6 (when the subarray is [4, -1, 2, 1]

my initial though:

BF?

but it will take too much time with O(n^2) time complexity
most likely to exceed the time limit as the given array gets longer in length

my second thought:

1. set the first element of the given list as a maximum in a new list (tabulation)
2. create a for loop from the next index to the last one
3. compare the value the last maximum plus the current element to the current element itself
4. if the former > latter:
    add the former to the new list
   else:
    time to set the starting point again by adding the value of the current index
5. return max(a new list) after iteration

"""
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        dp = [nums[0]]

        for i in range(1, len(nums)):
            res = dp[-1] + nums[i]

            if res <= nums[i]:
                dp.append(nums[i])
            else:
                dp.append(res)

        return max(dp)

# result - Runtime: 60 ms / Memory Usage: 14.6 MB, less than 81.26%
# time complexity: O(n) with one loop, space complexity: O(n) with a new array for dp

# better solutions from Python Algorithm Interview

# 1) an improved dp by reusing the given index
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

# 2) Kadane Algorithm
# : define two variables each for current max and total max
# compare the current max to the newly calculated variable then to the total max
# update if the current max exceeds the total max
# my immediate reaction to this was "IT IS BLOODY BRILLIANT". How can a person come up with such solutions
# it automatically changes the starting point

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maximize
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum

# both have the similar runtime with O(N) time complexity and O(1) space complexity