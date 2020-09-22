# https://leetcode.com/problems/intersection-of-two-arrays/

# Brute-Force can be used here

# Binary-Search:
# BS works only for a sorted array

# sort one array and create a loop with the other array
# compare each value of the other array to the sorted array with BS

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # a set to add intersections (to remove repetitive elements in an automatic way)
        ans = set()

        # sort one of the given array to use Binary Search
        nums2.sort()

        # iteratively take a look at each element of the other list as a target
        for target in nums1:
            # now below is the same process as Binary Search
            left = 0
            right = len(nums2) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums2[mid] == target:
                    ans.add(target)
                    break
                elif nums2[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return ans

# well, it kept giving me None as an output and turned out I did not write the last line (return ans)
# result - runtime: 52m/s(45.05%), memory usage: 14MB(38.09%)
# time complexity - I believe it should be O(n log n)? because a loop has O(n) and BS O(log n) / space complexity - O(n) to store date in a set (I might have been mistaken)

# Solution from PAI
# bisect can also be considered

import bisect

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # an array to add intersections
        result: Set = set()
        nums2.sort()

        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()

        # sort both arrays
        nums1.sort()
        nums2.sort()

        # two pointers
        i = j = 0

        # both arrays are sorted in ascending order
        # so if nums1[i] has a higher value, move j to the next or i if it's the other way round
        # if both have the same value, append one and move both pointers to the next together
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result
