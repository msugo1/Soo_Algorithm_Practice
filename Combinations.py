"""
the first try
- loop and create the list of 'n' numbers
- let's use a dict: key - sums (to sort out repetitive ones), and value - lists
, because a dict doesn't allow the same value for the same key. (but if the lists are the keys, it won't work
as lists will have different values in them)
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = {}
        nums = []
        prv = []
        res = []

        for num in range(n):
            nums.append(num + 1)

        def dfs(num_list):
            if k < 2:
                res.append(n)

            if len(num_list) == n - k:
                res.append(prv[:])

            for num in num_list:
                cur = num_list[:]
                cur.remove(num)

                prv.append(num)
                dfs(cur)
                prv.pop()

        dfs(nums)

        for combi in res:
            key = sum(combi)

            if key in ans:
                continue
            else:
                ans[key] = combi

        prv = []
        for value in ans.values():
            prv.append(value)

        return prv


"""
original plan - find possible combis with dfs, and remove redundancy by a dict

wrong - overlooked those combinatinos that have the same sums but not repetitive like [1, 4] and [2, 3]
key : value won't work unless chaining is implemented but it will store other repetitive combis
"""

"""
the second thought - might be able to narrow the range of numbers (ex. first loop 1~4 / second loop 2~4
or first 2~4 / second 3~4 like this)
"""

# couldn't come up with any way so I had a look at an explanation for this and it set a starting point as a parameter

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        element = []

        def dfs(num_list, start: int, k: int) -> List[int]:
            if k == 0:
                result.append(elements)

            for num in range(start, n + 1):
                elements = num_list[:]
                elements.append(num)
                k -= 1
                dfs(elements, start + 1, k)
                elements.pop()

        return result

# it returns nothing why..? well because I didn't really use dfs ;;
# anyways, it gave me a wrong answer [[1, 2], [2]] what's wrong here?


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(num_list, start: int, k: int) -> List[int]:
            if k == 0:
                result.append(num_list[:])

            for num in range(start, n + 1):
                elements = num_list[:]
                elements.append(num)
                # 'start + 1' needs to be replaced with 'num + 1' here because of the next range starts off with the number after I picked
                # above is done myself but couldn't really see the difference between k -= 1 first or just set 'k - 1' as a new parameter

                # k -= 1 isn't correct because when the loop starts again with another 'num (here 2)' the value of k won't be the same anymore in the first dfs operation.
                # so, when it goes to recursion again, k will already be 0, so it will just run the append operation straight away with '[2]'
                #
                dfs(elements, num + 1, k - 1)
                elements.pop()

        dfs([], 1, k)

        return result

# answer from python algorithm interview
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start: int, k: int) -> List[int]:
            if k == 0:
                result.append(elements[:])

            for num in range(start, n + 1):
                elements.append(num)
                dfs(elements, num + 1, k - 1)
                elements.pop()

        dfs([], 1, k)

        return result

# one line solution with itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums, 2)

"""
today's learning point
1. a = list_1 vs a = list_1[:] // the latter has a different reference, which means the amend of the original list (list_1) doesn't have any impact on it
2. itertools - especially itertools.combinations(), itertools.permutations()
"""