# https://leetcode.com/problems/number-of-1-bits/

# I guess it's similar to Hamming Distance that I did yesterday
# so it was the first solution that came to my mind.

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')

# result - runtime: 32m/s(61.99%), memory usage: 13.9MB(24.76%)

# what if I use only bit operations
# answer from Python Algorithm Interview

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:  # n > 0
            n &= n - 1
            count += 1

        return count

# similar runtime and memory usage

# I don't think I'm still getting the hang of bit manipulation, so need a lot of practice
