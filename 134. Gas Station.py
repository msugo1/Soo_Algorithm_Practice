# https://leetcode.com/problems/gas-station/
from math import inf
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        max_diff = -inf
        div = len(gas)
        fuel = 0

        for i in range(len(gas)):
            max_diff = max(max_diff, gas[i] - cost[i])

        if max_diff < 0:
            return -1

        starting_indices = []

        for i in range(len(gas)):
            if gas[i] - cost[i] == max_diff:
                starting_indices.append(i)

        for start in starting_indices:
            fuel += gas[start]
            helper = start

            while start != helper and start % len(gas) != helper:
                if fuel >= cost[start % len(gas)]:
                    fuel -= cost[start % len(gas)]
                    start += 1
                    fuel += gas[start % len(gas)]
                else:
                    break

            if start % len(gas) == helper:
                return helper

        return -1

# wrong answer - I suppose "while start != helper and start % len(gas) != helper:", this line has a problem

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        max_diff = -inf
        div = len(gas)
        fuel = 0

        for i in range(len(gas)):
            max_diff = max(max_diff, gas[i] - cost[i])

        if max_diff < 0:
            return -1

        starting_indices = []

        for i in range(len(gas)):
            if gas[i] - cost[i] == max_diff:
                starting_indices.append(i)

        for start in starting_indices:
            helper = start
            fuel += (gas[start] - cost[start])
            start += 1

            if start == len(gas):
                start = 0

            while start != helper:
                fuel += (gas[start] - cost[start])
                start += 1

                if start == len(gas):
                    start = 0

            if fuel >= 0:
                return helper

        return -1

# changed the middle part for a bit and still gave me a wrong answer
# case
# gas: [5, 8, 2, 8] / cost: [6, 5, 6, 6]
# expected 3 but output is 1

# invested almost 2~3 hours in this single question but couldn't figure out a proper condition for while in the second loop
# I feel like I can reach the answer but !!!! can't... so frustrated
# so I'll leave this question for tomorrow (or maybe i'll give it another try later today)

# 04 OCT 2020
# what I couldn't come up with: the range of indices, start ~ len(gas) + start means it will circle one loop
# also using boolean

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fuel = 0

        starting_indices = []

        for i in range(len(gas)):
            if gas[i] - cost[i] >= 0:
                starting_indices.append(i)

        if len(starting_indices) == 0:
            return -1

        for start in starting_indices:
            for i in range(start, len(gas) + start):
                location = i % len(gas)

                can_travel = True
                if fuel + gas[location] < cost[location]:
                    can_travel = False
                    break
                else:
                    fuel += (gas[location] - cost[location])

            if can_travel:
                return start

        return -1

# result - wrong answer, when gas = [5, 1, 2, 3, 4] / cost = [4, 4, 1, 5, 1]
# the output should be 4 but it returns 2
# spotted the reason - I did not reset fuel after a loop is done

# basically what I haven't been able to solve this problem since yesterday was because I forgot to reset fuel as 0 (regardless of the runtime)
# runtime is dreadful though... just flabbergasted for the fact that it did not exceed the time limit

# result: runtime - 8192m/s, 4532m/s (each 11% and 5%)

# well because it was O(n^2). There must be a way to make it a linear time complexity O(n)

# a solution from Python Algorithm Interview

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # can come back to the starting point only if the total amount of gas outstrips that of cost
        if sum(gas) < sum(cost):
            return -1

        # there must be ONE POINT of possibility, so if cost outpaces gas + fuel in the location,
        # exclude the location and move the starting point to the next
        # or keep adding fuel till the end
        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += (gas[i] - cost[i])

        # here, now what start points at should be the possible point
        return start
