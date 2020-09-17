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
            a = int(nums_1[i]) % 10 ** (len(nums_1[i]) - 1)
            b = int(nums_2[j]) % 10 ** (len(nums_2[j]) - 1)

            if a > b:
                merged_list.append(nums_1[i])
                i += 1
            else:
                merged_list.append(nums_2[j])
                j += 1

    return merged_list + nums_1[i:] + nums_2[j:]


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    # to string
    nums = [str(num) for num in nums]

    mid = 0 + len(nums) - 1

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