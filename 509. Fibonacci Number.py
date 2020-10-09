# https://leetcode.com/problems/fibonacci-number/

# it can be solved by DP(Dynamic Programming as it has both Optimal Substructure and Overlapping Sub-problem
# it saves us so much time to save the previous results because the calculating process takes place only once
# which would keep happening till our code reaches the answer otherwise
# memoisation, tabulation (top-down, bottom-up)
# the former is implemented by recursion whereas the latter by iteration

# 1. normal recursion
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        return self.fib(N - 1) + self.fib(N - 2)

# 2. memoisaition
# add a dictionary to save the results, so if N is already in there, the result will be reused without calculating it again
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        if self.dp[N]:
            return dp[N]

        return self.fib(N - 1) + self.fib(N - 2)

# 3. tabulation
# the indices 0, 1, have exception cases so put them in an array in advance and update from index 2 with the previously calculated values
class Solution:
    def fib(self, N: int) -> int:
        dp = [0, 1]

        if N < 2:
            return dp[N]

        for i in range(2, N + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[N]


# 4. just update two variables each time (it's both saving time and space - O(n), O(1))
class Solution:
    def fib(self, N: int) -> int:
        x, y = 0, 1

        for i in range(0, N):
            x, y = y, x + y

        return x