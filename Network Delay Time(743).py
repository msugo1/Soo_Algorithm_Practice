# https://leetcode.com/problems/network-delay-time/

# (u, v, w) - u: the source node, v: the target node, w: time it takes from the source to target
# dijkstra Algorithm will do

# visited, unvisited
# graph = collections.defaultdict(list) - graph[u] = [[v, w]]  or graph[:1].append[1:]?
def network_delay_time(times):
    graph = collections.defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))

    return graph

time = [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]]

print(network_delay_time(time))
