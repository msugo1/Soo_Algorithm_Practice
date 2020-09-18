# https://leetcode.com/problems/largest-number/

# sort with the biggest remains  by %10?
# with the same remain - put priority on bigger nums?
# not working - exception = [3, 90, 890]
# because 890 > 90 but 90890 > 89090...

# numbers only with units seem to have priority (a > ab, aab > aba)
# except if (b is bigger than a, then aba > aab)

# well I guess I kinda worked it out that merge sort (O(nlogn)) would probably work

# so logic for merge_sort function would be
# turn the list to string, divide them into two parts: left and right, then merge - recursion

# for merge function:
# using place value seems valid
# the elements of the given list already got turned into a string by like [str(a) for a in nums]
# so len - that gives place value out - is possible to be made use of
# if len (place value) for the both numbers are down the same, now check bigger nums by int( ),
# and add the bigger one in a new_list called merged_list, as well as give the index for the target list +1
# then add all the rest of the part to the completed list after the process above and return

# put the given list in merge_sort and then combine the result together into one string

a = [3, 30, 34, 5, 9]


def largestNumber(nums):
    if nums:
        res = merge_sort(nums)
        return res


def merge(nums_1, nums_2):
    merged_list = []

    i = 0
    j = 0

    while i < len(nums_1) and j < len(nums_2):
        if len(nums_1[i]) == len(nums_2[j]):
            if int(nums_1[i]) > int(nums_2[j]):
                merged_list.append(nums_1[i])
                i += 1
            else:
                merged_list.append(nums_2[j])
                j += 1
        else:
            if len(nums_1[i]) == 1:
                a = int(nums_1[i])
            else:
                a = int(nums_1[i]) % 10

            if len(nums_2[j]) == 1:
                b = int(nums_2[i])
            else:
                b = int(nums_2[j]) % 10

            if a > b:
                merged_list.append(nums_1[i])
                i += 1
            else:
                merged_list.append(nums_2[j])
                j += 1

    if i == len(nums_1):
        merged_list += nums_2[j:]
    elif j == len(nums_2):
        merged_list += nums_1[i:]

    return merged_list


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    # to string
    nums = [str(num) for num in nums]

    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    return merge(left, right)

print(largestNumber(a))

# executed this before join the strings in the list together and got the weird result why?
# result = ['10', '2'] when the list is [10, 2]
# result = ['9', '3', '30', '34', '5'] when the list is [3, 30, 34, 5, 9]

# !!! 10 ** len(a) was supposed to give the wrong result as it means an element would be divided not by its place value
# but by place value * 10 (one higher)

# a = int(nums_1[i]) % 10 ** len(nums_1[i])
# b = int(nums_2[j]) % 10 ** len(nums_2[j])

# here both 10 ** len(nums_1[i]), and 10 ** len(nums_2[j]) should be len( ) - 1
# not working okay now I'm frustrated

# 10 ** (len(nums_1[i]) - 1) shouldn't be 1 because everything % 1 will come down to 0

# just looked through the process and totally wrong.
# so many exceptions... I'll try it again tomorrow.

# hint: whilst merging [a] - [b]
# [ab] > [ba] or [ab] < [ba]

# found another mistake, merge_sort was not calling recursive functions...
# it was left = nums[:mid], right = nums[mid:] which should have been left = merge_sort(nums[:mid]), merge_sort(right = nums[mid:])

# found an interesting fact that if mid is len(list) - 1 // 2, it causes maximum recursion error but if it is len(list) // 2,
# calls recursion correctly

# what's the difference? maybe it would be another homework

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = self.merge_sort(nums)
        return str(int("".join(map(str, res))))

    def merge(self, nums_1, nums_2):
        merged_list = []

        i = 0
        j = 0

        while i < len(nums_1) and j < len(nums_2):
            if int(str(nums_1[i]) + str(nums_2[j])) > int(str(nums_2[j]) + str(nums_1[i])):
                merged_list.append(nums_1[i])
                i += 1
            else:
                merged_list.append(nums_2[j])
                j += 1

        return merged_list + nums_1[i:] + nums_2[j:]

    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums

        # to string
        mid = len(nums) // 2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)

# finally passed all the cases
# result: runtime 44m/s (54.23%) / memory usage: 13.8mb
# return str(int("".join(map(str, res)))) for this line, I had no idea how to deal with the input [0, 0]
# whose output should have been '0' rather than '00' so I had to look up some info
# ("".join(map(str, res)) means the output will be '00' so change it to int to make it 0 and then again to str

# a solution from PAI: solved the question with insertion sort
class Solution:
    def to_swap(self, n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))
# amend 'nums[j - 1] > nums[j]' to 'self.to_swap(nums[j - 1], nums[j])' to write a concise code
# How could the author even think of a code like this?
# Would it be possible for me to take my coding skill to this level if I practice a lot?

# a key point to this question.
# Can you think of a logic that str(a) + str(b) < str(a) + str(b) or vice versa (a, b : int)