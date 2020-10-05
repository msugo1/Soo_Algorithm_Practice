# https://leetcode.com/problems/majority-element/

# first thought - why don't I use collections.Counter
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

# result - Runtime: 156ms(98.12%), Memory Usage: 15.3MB(33.33%)
# It worked and it has a spectacular runtime but this chapter is all about divide and conquer, which is normally done by recursion
# so, I'll have another go recursively this time

# description: The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# which means when they are sorted, it will have the one (the number that's majority) right in the middle

"""
(divide)
base case
: len(nums) == 1

recursive case

mid = left + right // 2
left_half = ~ mid
right_half = mid + 1 ~

(conquer)
merge

then return the one in the middle
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def merge(arr1, arr2):
            merged_arr = []

            i, j = 0, 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    merged_arr.append(arr1[i])
                    i += 1
                else:
                    merged_arr.append(arr2[j])
                    j += 1

            return merged_arr + arr1[i:] + arr2[j:]

        def merge_sort(arr):
            # base_case
            if len(arr) < 2:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        merged_list = merge_sort(nums)
        return merged_list[len(nums) // 2]

# it did the job but took too long
# result - runtime: 500ms(5.36%), memory usage: 16.2MB(5.28%)
# must be a way to optimise

# solutions from Python Algorithm Interview
# 1) Dynamic Programming (with memoisation)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)

        for num in nums:
            if counts[num] == 0:
                # if not counted yet, count the number and then store the result in a dict
                counts[num] = nums.count(num)

            # if count[num] has a higher number than the half of the arr length, it means it's the majority
            if counts[num] > len(nums) // 2:
                return num

# result - Runtime: 152 ms, faster than 99.05% / Memory Usage: 15.4 MB, less than 5.76%

# 2) Divide and Conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

# result - Runtime: 232 ms, faster than 19.07%, Memory Usage: 15.5 MB, less than 5.28%
# it's an optimised take on of the second process of mine
# well, apparently, the whole elements do not need to be rearranged but only the majority part

#        if len(nums) == 1:
#            return nums[0]

# here return nums[0] is to pick out only an integer (ex. 3) not an element of a list (ex. [3])

# 3) sort the given arr with a built-in sort method then return the value on mid index
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]