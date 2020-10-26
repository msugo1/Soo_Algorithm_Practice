# https://leetcode.com/problems/two-sum/

# only one valid answer exists
# which means if I can find target - a value in the list but from the next index
# add it to an empty list and then change target to target - a value
# then when the modified target equals another value, add it and return

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        for i, v in enumerate(nums):
            if len(ans) == 1:
                if target == v:
                    ans.append(i)
                    break
            else:
                another = target - v
                if another not in nums[i + 1:]:
                    continue
                else:
                    ans.append(i)
                    target = another

        return ans

# result: Runtime: 1036 ms
# I clearly remember not being able to solve this problem when I tried Leetcode for the first time
# even after spending a good couple of days
# I did solve it on my own this time but not happy about the result... There must be multiple ways
# to reduce the execution time
# I'll leave it for today here and then probably try it tomorrow or couple days later
