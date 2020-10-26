# https://leetcode.com/problems/valid-palindrome/

import re

# revise Q1
# regular expression would do to remove anything else rather than alphabet or possibly digit?
# re.sub

Input = "A man, a plan, a canal: Panama"

# re.sub(pattern, replacement, string)
# ^ means 'not'
sub = re.sub('[^a-zA-Z0-9]', '', Input)

# reverse with list slicing [::-1] for strings

# case 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub('[^a-zA-Z0-9]', '', s)
        return s == s[::-1]

# case 2: turn a string into a list with some conditions
# here .isalnum() (if it's alphanumeric)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []

        for char in s:
            if char.isalnum():
                res.append(char.lower())

        char = ''.join(res)
        return char == char[::-1]

#       OR
#       while len(res) > 1:
#           if res.pop() != res.pop(0):
#               return False
#       return True
# pop both ends and compare (so deque would be way more efficient here)
