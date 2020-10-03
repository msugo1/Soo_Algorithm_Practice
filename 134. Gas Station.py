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

