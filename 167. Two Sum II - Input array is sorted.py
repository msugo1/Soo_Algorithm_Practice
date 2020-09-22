# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# two pointer again

# both arrays are sorted given in ascending order
# so if nums1[i] has a higher value, move j to the next or i if it's the other way round
# if both have the same value, append one and move both pointers to the next together

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:  # while not left == right in the book
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

# result - runtime: 60m/s(90.90%), memory usage: 14.4(25.81%)

# what if with Binary Search?
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, one in enumerate(numbers):
            the_other = target - one
            left, right = 0, len(numbers) - 1

            while left <= right:
                mid = left + right - left // 2
                if numbers[mid] < the_other:
                    left = mid + 1
                elif numbers[mid] > the_other:
                    right = mid - 1
                else:
                    return [k + 1, mid + 1]

# result - time limit exceeded
# left = k + 1 (instead of left = 0) solves the problem
# why? well, if a pair for the answer was found with the indices before, it will already be returned
# so, the speed increases by removing the redundant process - comparing from the beginning


