"""
case 1: s is palindrome itself
if s == s.reverse()
    return s

case 2: len(s) < 2:
    return s

case 3: normal
the first thought
- could go with two iteration

create an empty string to store the longest palindrome outside (global variable)
another empty string for local variable

if global palindrome < local palindrome - update

it would seem to work well but with O(n^2) time complexity
"""


class Solution:
    longest = ""

    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1] or len(s) < 2:
            return s

        for i in range(len(s)):
            local_longest = ""
            for j in range(i, len(s)):
                local_longest += s[j]
                if local_longest == local_longest[::-1] and len(local_longest) > len(self.longest):
                    self.longest = local_longest

        return self.longest

# result - Runtime: 6576 ms, faster than 18.34%, Memory Usage: 14.3 MB, less than 48.80%
# it was just fortunate that the code above passed the whole cases. It could've been just time limit exceeded
# so, it definitely needs improving in time complexity, but how?

# maybe two pointers? this idea has just occurred to me
# but then which should be narrowed down first, left or right?
# I was thinking only of right coming toward the left pointer first and then left in turns but the result would probably
# say"abacab" doesn't have "bacab" as the longest palindrome

# Why couldn't I come up with the idea of starting from the middle! now inspired by Python Algorithm Interview

# never knew creating a helper method would do
# been pondering this question quite a while and then couldn't still think of the answer so had to refer to the book and
# explanations on Youtube.

# Now, I get how the two pointers with the method within it works.
# i, i for odd numbers whereas i, i + 1 works for even numbers

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        res = ''
        for i in range(len(s)):
            if len(res) < len(helper(i, i)):
                res = helper(i, i)
            if len(res) < len(helper(i, i + 1)):
                res = helper(i, i + 1)

        return res
