# https://leetcode.com/problems/minimum-window-substring/
# time complexity should be O(n)

# first try
# set two pointers as i, j for 0 each
# check if t is in [i:j+1]
# move j to the next - j += 1 if t not in the sliced string above
# else - check which is longer(the previously stored substring vs a new one)
# swap it if the latter has a short length

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_substring(condition, sliced_string):
            for element in condition:
                if element not in sliced_string:
                    return False
            return True

        if not s or not t:
            return ""

        i = 0
        j = 0
        res_str = s

        while j < len(s):
            sub_string = s[i: j + 1]
            if t not in sub_string:
                j += 1
            else:
                if len(sub_string) < len(res_str):
                    res_str = sub_string
                i += 1

        if res_str != s:
            return res_str
        else:
            return ""

# problem - not just s but the code should check if each component of T in S
# can I use for within while? that would be O(n^2) tho...


# add a function to see if the sliced_string contains all the components of t
def is_substring(condition, sliced_string):
    for element in condition:
        if element not in sliced_string:
            return False
    return True

# then make use of it
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_substring(condition, sliced_string):
            for element in condition:
                if element not in sliced_string:
                    return False
            return True

        if not s or not t:
            return ""

        i = 0
        j = 0
        res_str = s

        while j < len(s):
            sub_string = s[i: j + 1]
            if is_substring(t, sub_string):
                if len(sub_string) < len(res_str):
                    res_str = sub_string
                i += 1
            else:
                j += 1

        if res_str != s:
            return res_str
        else:
            return ""

# pass the test case "ADOBECODEBANC", "ABC" // but failed "a", "a"

#         if is_substring(t, res_str):
#             return res_str
#         else:
#             return ""

# correct the last part to check res_str again in case j's reached at the end because simply t not in s:

# wrong answer: "aa" "aa" - return "" // ""bbaa"" "aba" - return "ba"
# seems I must deal with repetitive strings
# maybe turn the sub_string into a list and pop the already seen elements out or change the range?

#           def is_substring(condition, sliced_string):
#             string_list = list(sliced_string)
#
#             for element in condition:
#                 if element not in string_list:
#                     return False
#                 string_list.remove(element)
#             return True

# the added condition above (turning a string into a list and pop the element out) enabled me to pass 267/268
# now time limit exceeded with the ludicrously humongous input

# now need to have a look where I could possibly reduce the time complexity

# hint from Python Algorithm Interview - collections.Counter
# need - collections.Counter(t), missing - len(t)

