# https://leetcode.com/problems/binary-search/
# just how to implement binary search

# 1) recursion 2) iteration

# 1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            # only valid whilst left <= right
            if left <= right:
                # set a mid index
                # return mid if mid index is on the target
                # search again from left to mid - 1 if mid index is on a higher value than the target
                # the same but from mid + 1 to right for the last case
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return binary_search(mid + 1, right)
            # if left index has a higher value than right index and still target is not found - it does not exist(false)
            else:
                return -1

        return binary_search(0, len(nums) - 1)

# 2)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # basically similar to recursion
        # mid determines left or right
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

# two other solutions from PAI
# 3) I did not know that but python boasts its own binary search  module
# the book said the module even excludes various exceptions itself
# it is 'bisect'

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

# 4) seems like index function can replace bisect or binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

# pleasantly surprised by Python that seems bottomless

# mid = (left + right) // 2

# this formula can pose problems in other languages such as C or Java as int can have/express a value only up to 2^31 -1
# Overflow will be brought about if left + right outstrips such limit

# Python has no problem with it but more accurate code would be:

# mid = left + (right - left) // 2

# both do not exceed the limit