# https://leetcode.com/problems/combination-sum/
import collections


# first try
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # answer_list
        ans = []
        # store counter.dict data to avoid duplicate combinations like 2, 2, 3 and 3, 2, 2 have the same counts in elements.
        count = []

        def dfs(elements, target_sum):
            # sum over target - returns none
            if sum(elements) > target_sum:
                return
            # sum equals target - only if counted elements by Counter not in count - add both a Counter and list
            elif sum(elements) == target_sum:
                count_elements = collections.Counter(elements)
                if count_elements not in count:
                    count.append(count_elements)
                    ans.append(elements[:])
            # sum below target - repeat the same procedure
            for num in elements:
                elements.append(num)
                dfs(elements, target_sum)
                elements.pop()

        dfs([], target)
        return ans


# it doesn't add any lists in ans... what did I get wrong here?

# second try
# just realised I haven't actually used the given list 'candidates' but instead an empty list haha
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        count = []
        res = []

        def dfs(nums, combinations):
            if sum(combinations) > target:
                return

            elif sum(combinations) == target:
                count_elements = collections.Counter(combinations)
                if count_elements not in count:
                    count.append(count_elements)
                    res.append(combinations[:])
                else:
                    return

            for num in nums:
                combinations.append(num)
                dfs(nums, combinations)
                combinations.pop()

        dfs(candidates, [])
        return res


# Success - Runtime: 808ms (faster than 5%) / Memory Usage: 14MB (less than 30.74%)
"""
managed to solve this problem, but it has around 800ms runtime speed, which is really slow.
There must be a plethora ways to improve or just better algorithms for this.
Let's give it a try to come up with a better answer for today and
if not possible, refer to others' codes or the one in Python Algorithm Interview
"""

# the third try with python algorithm interview
"""
what I've understood so far: 
1. target - a value of the given list till it gets 0 and then stop with return 
otherwise, it would be running forever
2. simple index controls can keep from getting duplicates

the previous index has nothing to do with the next indices

ex. [2, 3, 6, 7] after picking out 2, 3 from the list, index 0 doesn't have to be seen 
because [2, 3, 2] is already there as [2, 2, 3]

3. run the append operation in the parameter
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # csum = a short form of candidate sum
        def dfs(csum, index, path):
            # to get rid of infinite loop
            if csum < 0:
                return
            elif csum == 0:
                res.append(path)
                # to save this function a redundant recursion again
                return

            # range - from the index to the length of the given list
            # against generating duplicates
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])  # list sum takes only between a list and list

        dfs(target, 0, [])
        return res

# Result - Runtime: 76ms (faster than 72.85%) / Memory Usage: 13.7MB (less than 92.33%)
# above saved huge amount of time by not carrying out unnecessary repetitive procedures
# such as checking if an answer has the same values as the previous one with Counter I did with a simple index control
# or even saved space not making another list

# today's learning point
# 1. index control
# 2. how to reduce unnecessary process like by running append in parameters
