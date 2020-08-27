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

