# https://leetcode.com/problems/hamming-distance/

"""
- each number has its own binary representation
- ^ (XOR) operator will probably tell the difference by changing not the same combi (0, 1 or 1, 0) at the same place value

- turn the result into a string and + count if that value is 1 in a for loop
- return count
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        str_bin = str(bin(x ^ y))

        for digit in str_bin:
            if digit == '1':
                count += 1

        return count
# result - runtime: 28m/s (78.49%), memory usage: 13.7MB(81.81%)
# seems like numbers represented in binary system are considered a string
# str(bin(x ^ y)) isn't required then.

# count can be used here, one line solution from Python Algorithm Interview
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
# result - runtime: 20m/s (98.51% wow!)