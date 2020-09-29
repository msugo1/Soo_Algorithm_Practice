# https://leetcode.com/problems/longest-repeating-character-replacement/

# Figuring out how to approach this question is giving me a headache
# store indices in dictionary and see the difference among the indices if less than k?
# does not seem plausible nor promising

# what if, setting i, and j...
# i = 0 ~ len(s) / j = i + 1 ~ len(s)
# previous = s[i]
# if previous is not the same as the current, take 1 from k / iterate till k gets to 0
# update previous, and maximum_length
# sounds alright except it will have O(n^2) in time complexity

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        k_reset = k
        length = 1

        i = 0
        j = 0
        prev = 0

        for i in range(len(s)):
            prev = s[i]
            j = i + 1
            length = 0
            while j < len(s) or k > 0:
                if s[j] != prev:
                    k -= 1
                length += 1
                j += 1

            max_len = max(max_len, length)

            if max_len > len(s[i + 1:]):
                break
            else:
                k = k_reset

        return max_len

# result - index out of range: if s[j] != prev this part

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        k_reset = k
        length = 0

        j = 0
        prev = 0

        for i in range(len(s)):
            prev = s[i]
            j = i
            length = 0
            while j < len(s) and k > 0:
                if s[j] != prev:
                    k -= 1
                length += 1
                j += 1

            max_len = max(max_len, length)

            if max_len > len(s[i + 1:]):
                break
            else:
                k = k_reset

        return max_len

# correct some line length to 0, j < len(s) or k > 0 to 'and'
# passed 17 cases out of 37
# wrong answer for the case where s = "AABABBA" and k = 1

# found out the code above can't deal with cases like k's already reached 0 but still some same letters exist consecutively from there

# a hint from Python Algorithm Interview = the right pointer - left one - most common == k

# sliding window - keep moving i till right - left > k, which means now it's over k's capacity
# use Count here and keep tracking the number of letters within the range (left ~ right)
# move left to left + 1 with the exclusion of an element on left

# Finally understood the logic with the explanation from the book so I'll give it a try to implement later
