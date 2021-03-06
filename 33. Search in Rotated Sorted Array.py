# https://leetcode.com/problems/search-in-rotated-sorted-array/

# couldn't come up with the best idea for a pivot in this question
# which led me to have a look at the book, PYI

# It suggested picking out an index of the minimum value as a pivot
# I wondered why and now that I think about it, it is probably because the both left and right sides from the pivot
# will be sorted again in an ascending order

# so if target equals the value on the pivot, it will be returned
# or pick just an appropriate side of the two and then iterate till the target index is found
# or return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the minimum value for a pivot
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        if nums[pivot] == target:
            return pivot
        else:
            if nums[0] <= target < nums[pivot - 1]:
                left, right = 0, pivot - 1
            elif nums[pivot + 1] <= target < nums[len(nums) - 1]:
                left, right = pivot + 1, len(nums) - 1
            else:
                return - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

# result: list index out of range
# this part: elif nums[pivot + 1] <= target < nums[len(nums) - 1]:
# exception: [1, 2, 4, 5, 6, 7, 0] - when pivot is the last

# added another condition - pivot != len(nums) - 1 and nums[pivot + 1] <= target <= nums[len(nums) - 1]:

# it returns -1 when nums = [1, 3] and the target = 3 are... should have been 1
# I don't have days so give another try tomorrow

# low ~ mid ~ high
# if nums[mid] == target return mid
# if nums[low] < nums[mid]
# if nums[low] <= target <= nums[mid]
# change high to mid - 1 (mid is supposed to be already seen above)
# otherwise, swap low to mid + 1

# else (nums[low] > nums[mid])
# if nums[mid] <= target <= nums[high]
# high = mid - 1
# else change low to mid + 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[low] < nums[mid]:
                if nums[low] <= target <= nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

# result = wrong answer

# answer from PAI
# with another pivot in the answer called mid_pivot

# mid_pivot = (mid + pivot) % len(nums)

# left = mid + 1 if nums[mid_pivot] <= target else right = mid - 1
# honestly, I don't think I understood the logic of this. I'll keep this for later.
