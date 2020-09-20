# https://leetcode.com/problems/k-closest-points-to-origin/

# sorted with lambda by the distance from (0, 0)
# so key for sorting is sqrt((x[0] - 0) ** 2 + (x[1] - 0) ** 2)

import math, heapq

nums = [[3, 3], [5, -1], [-2, 4]]

sorted_list = sorted(nums, key=lambda x: math.sqrt(x[0]**2 + x[1]**2))

print(sorted_list)

# it worked so the general code would be

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: math.sqrt(x[0]**2 + x[1]**2))[:K]

# sorted by one-line (I would say it is quite pythonic)
# result: runtime(716m/s - faster than 73.15%)


# solution from Python Algoritm interview
# by 'Priority Queue' (cus the question asks 'extraction' k times)

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            # math.sqrt can be left out here because the result itself is not used anywhere else
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append([x, y])
        return result

# or this line 'heapq.heappush(heap, (dist, x, y))' can change to [dist, [x, y]]

#             (dist, x, y) = heapq.heappop(heap)
#             result.append([x, y])

# so it can be just one line: result.append(heapq.heappop(heap)[1])
# it is from a post of the discuss section on leetcode
# I personally find it more straight-forward than the two lines above
