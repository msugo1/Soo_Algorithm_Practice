# the first try
# creat a list (ans) and pass a list with an added value onto the recursive function as a parameter (fail)
def permute(self, nums: List[int]) -> List[List[int]]:
    def dfs(nums, ans):
        # base_case
        if len(nums) == len(ans):
            return ans

        # recursive_case
        for num in nums:
            ans.append(num)
            dfs(nums, ans)

# the second try
# realised that well in the second loop the list will be like [a, b ~ ] but not [b ~] (the first value remains)
# need another approach
# values are not even added to the prev list either wth
def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []
    num_list = nums
    prev = []

    def dfs(num_list, collection):
        # base_case
        if len(num_list) == len(prev):
            ans.append(prev)
            return
        # recursive_case
        for num in num_list:
            if num in prev:
               continue
            else:
                prev.append(num)
                dfs(nums, prev)

        return ans

# the third try with referring to an explanation in python algorithm interview
# I was thinking maybe I could move an element of the given num_list to another list and then use 'not in' for the next
# but I could've just deleted(or removed) the element

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prv = []

        # take lists of each stage for nodes. The nodes will be leaf nodes at the last level
        # add when it's a leaf node
        def dfs(elements):
            if len(elements) == 0:
                res.append(prv[:])

            for e in elements:
                # [:] enables a list to copy with a different reference - means correcting the list doesn't affect the original
                cur = elements[:]
                cur.remove(e)

                prv.append(e)
                dfs(cur)
                # what I understand:
                # first '1' will be added to prv, and recursion automatically complete the other process and make [1, 2, 3] out of it
                # but from the next, prv will have another value at the end that should've been deleted in the previous loop
                # like when '2' should be added in prv (previously empty) '1' will remain and the same goes for the whole
                prv.pop()

        dfs(nums)
        return res

# refer to 'itertools', especially 'itertools.permutations()'