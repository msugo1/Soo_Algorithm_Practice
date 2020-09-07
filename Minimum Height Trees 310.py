# https://leetcode.com/problems/minimum-height-trees/

# first try
# Let's see if defaultdict(list) and queue can be used
# like  0: [1]
#       1: [2, 3]
# or
#       1: [0, 1, 2]

import collections

# worked on this problem for an hour and half but still I came up with only making it a graph and then create a queue then delete what's already visited
# but not be able to picture the necessary procedure
# got a hint from PAI - remove leaf nodes step by step and then create a tree with the remaining center node of a graph
# because that would mean it's connected to as many nodes as possible, so will be minimum in height

def find_min_height_trees(n: int, edges: list):
    # create a graph
    graph = collections.defaultdict(list)

    for element in edges:
        graph[element[0]].append(element[1])
        graph[element[1]].append(element[0])

    # the result of an example

    # 1: [3],
    # 3: [1, 2, 4, 5],
    # 2: [3],
    # 4: [3, 6],
    # 5: [3, 7, 8],
    # 6: [4, 10],
    # 10: [6],
    # 7: [5],
    # 8: [5, 9],
    # 9: [8]

    # find leaf nodes
    # one element in a list means a leaf node

    # leaf_node = []
    # for key, value in graph.items():
    #     if len(value) < 2:
    #         leaf_node.append(key)
    #         del graph[key]
    # Traceback (most recent call last):
    #   File "C:/Users/고명수/Desktop/Algorithm Practice/test.py", line 15, in <module>
    #     for key, value in graph.items():
    # RuntimeError: dictionary changed size during iteration

    leaf_nodes = []
    for key, value in graph.items():
        if len(value) == 1:
            leaf_nodes.append(key)

    # leaf_node will have [1, 2, 10, 7, 9]
    # now delete these from the graph
    # and I couldn't work it out from here so had to refer to the hint from the PAI book
    # need to iterate the precess till n becomes 2

    # while n > 2:
    #     n -= len(leaf_nodes)
    #     for leaf in leaf_nodes:
    #         if leaf in graph:
    #             del graph[leaf]
    #
    #         for key, value in graph.items():
    #             if leaf in graph[key]:
    #                 graph[key].remove(leaf)

    # while n > 2:
    #     n -= len(leaf_nodes)
    #     new_leaf_nodes = []
    #
    #     for leaf_node in leaf_nodes:
    #         neighbour = graph[leaf_node].pop()
    #         graph[neighbour].remove(leaf_node)

    # couldn't still figure out how to delete keys and values of the counterparts in a dictionary
    # so I, ended up haivng to have a look at the answer
    # I wish I could come up with this brilliant process on my own

    while n > 2:
        n -= len(leaf_nodes)
        new_leaf_nodes = []

        for leaf_node in leaf_nodes:
            # here I was trying to remove keys itself in a list of the first leaf nodes
            # but it caused problems afterwards, no idea how to sort out the next leaf nodes and
            # how to swap the list of leaf nodes with a fresh one
            neighbour = graph[leaf_node].pop()
            graph[neighbour].remove(leaf_node)

            if len(graph[neighbour]) == 1:
                new_leaf_nodes.append(neighbour)

        leaf_nodes = new_leaf_nodes

    return leaf_nodes

# I took a look at the answer in the end but there are still some that I couldn't get my head around
# so, definitely should think about this question a bit more tomorrow