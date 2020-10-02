# https://leetcode.com/problems/task-scheduler/
import collections
from typing import List

"""
times = 0

counter(to count the number of each task)

choose from the most common - a short cut to the least possible trials

while n > 0:
    if n != 0 and only prev == curr left (everything else's count is zero):
        just times += 1
    
n = 2 (n reset - probably need to set another variable for the initial n value)
            
start from the beginning till everything becomes 0 in tasks

"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # prev = 0
        times = 0
        reset = n

        i = 0

        while tasks:
            prev = 0

            while n >= 0 and i < len(tasks):
                curr = tasks[i]

                if curr != prev:
                    n -= 1
                    prev = curr
                    times += 1
                    tasks.remove(curr)

                i += 1

            n = reset
            i = 0

        return times

# result - wrong answer(output 6, expected 8)
# I could not implement my logic set, so had to refer to Python Algorithm Interview

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                # it was what I was looking for, basically same as counter['task'] -= 1
                counter.subtract(task)

                # a life hack, it removes keys that have 0 as their value
                counter += collections.Counter()

            if not counter:
                break

            # add idle
            result += n - sub_count + 1

        return result