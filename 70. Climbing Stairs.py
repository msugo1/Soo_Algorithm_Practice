# https://leetcode.com/problems/climbing-stairs/
"""
possible steps = 0, 1, 2
n = top

how many steps will it take to the top with those three possible steps

n = 1
1 - 1

n = 2
1, 1 - 2
0, 2 - 2

n = 3
1, 2 - 3 (n = 1 case + 2)
1, 1, 1 (n = 2 case + 1)
0, 2, 1 (n = 2 case + 1)

n = 4
1, 1, 2 (n = 2 case + 2)
0, 2, 2 (n = 2 case + 2)

1, 2, 1, 1 (n = 3 case + 1)
1, 1, 1, 1 (n = 3 case + 1)
2, 1, 1 (n = 3 case + 1)


conclusion: f(n) = f(n - 1) + f(n - 2)

basically the same as fibonacci in a different form
"""

# 1) simple recursive

# 2) memoisation
import collections


class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]

# 3) tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        possible_steps = [0, 1, 2]

        if n <= 2:
            return possible_steps[n]

        for i in range(2, n):
            possible_steps.append(possible_steps[i] + possible_steps[i - 1])

        return possible_steps[n]

""" result

1) simple recursion 
: time limit exceeded

2) memoisation
: Runtime: 32 ms, faster than 47.17%
Memory Usage: 14.1 MB, less than 99.98%

3) tabulation
: Runtime: 28 ms, faster than 75.68%
Memory Usage: 14.1 MB, less than 99.98% 
"""