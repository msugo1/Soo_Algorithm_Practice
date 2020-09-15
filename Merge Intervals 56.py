# https://leetcode.com/problems/merge-intervals/

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# it means list should be sorted first by the first element on each index
# sorted(intervals, key:lambda x: x[0])

# first I tried with merge sort but couldn't go further when encountering not overlapped lists.

# took a hint from the book.
# create a list (merged) and add(append) an element from the given list(intervals) first
# then compare the last one from merged and a new one from intervals in a loop

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        for i in sorted(intervals, key=lambda x: x[0]):
            # i[0] (new one) is lower than merged[-1][0] (old one) means these two can be merged into one
            if merged and i[0] <= merged[-1][1]:
                # replace the one in merged, the first element with the lower one of either i[0] or merged[-1][0]
                # the second element with the higher one of either i[1] or merged[-1][0]
                merged[-1] = [min(i[0], merged[-1][0]), max(i[1], merged[-1][1])]
            else:
                # no overlap means it just can be added to the list directly
                merged.append(i)

        return merged

# runtime: 92ms (65.88%)

# sorted(intervals, key=lambda x: x[0])
# !! it means the list above is sorted by the first element of each element list and
# the first value of the next one can't be lower than that of the previous one

# merged[-1] = [min(i[0], merged[-1][0]), max(i[1], merged[-1][1])] can be shortened like this
# [-1][0] doesn't need to be replaced but only [-1][1] with the higher one

merged[-1] = [min(i[0], merged[-1][0]), max(i[1], merged[-1][1])] ->

    merged[-1][1] = max(i[1], merged[-1][1])

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)

        return merged

# more concise code
# but i don't know why it takes more time (runtime: 148ms - around 20%)
