# https://leetcode.com/problems/course-schedule/
# can't even understand what the question means at all
# I'd rather watch an introductory video with regard to topological sort
# got the gist of it but still can't get my head around the question

""""
        from what I've got so far
1) create a graph with a dict(defaultdict)
2) search the graph with dfs (visited, and stack)
    2-1 if the graph has a cycle - false
    2-2 else - go to 3
3) stack to ans
4) len(ans) == numCourses ?
"""

import collections

a = [[1, 0], [0, 1], [1, 0], [0, 1]]
#
# # graph = collections.defaultdict(list)
# #
# # for x, y in a:
# #     graph[x] = y
# #
# # print(graph)

# result - {1: 0, 0: 1} // not just values but also keys that are not stored with the same variables
# not sure of what the input is like but I'm assuming it should be like [1, 0] [0, 1] [1, 2] etc then
# wait just realised the value is 'list' so should use 'append'

# first try
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = []
        finished = []

        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(course, course_graph, taken, stack):
            curr = course_graph[course][0]

            if not curr:
                taken.append(course_graph[course].pop(0))
                dfs(curr, course_graph, taken, stack)
            else:
                if taken:
                    stack.append(taken.pop())
                    dfs(taken[-1], course_graph, taken, stack)
                else:
                    return taken

        dfs(0, graph, visited, finished)
        return len(finished) == numCourses

# Rumtime Error - list index out of range
# curr = course_graph[course][0], this line is posing a problem
# second try with the book's help
# not really knew where it went

# third try / this time kahn's sort with indegree and outdegree
# I'll try this problem later
