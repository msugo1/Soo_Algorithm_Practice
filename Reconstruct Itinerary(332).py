# https://leetcode.com/problems/reconstruct-itinerary/
# first try
# logic - make a func add items that contain "JFK" on their first index [0] and sort them with lambda
# in another func - add the first value of an item to the answer list and put the second one again in the func above
# in order to get an item of a list that starts with the second value
# that will be again what we are looking for straight away because the func automatically sorts items out

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []

        def find_earliest_ticket(ticket_list, departure_point):
            departure_list = []

            for ticket in ticket_list:
                if ticket[0] == departure_point:
                    departure_list.append(ticket)

            return sorted(departure_list, key=lambda x: x[1])[0]

        departure = find_earliest_ticket(tickets, "JFK")
        ans.append(departure[0])
        tickets.remove(departure)

        while tickets:
            departure = find_earliest_ticket(tickets, departure[1])
            ans.append(departure[0])
            tickets.remove(departure)

        ans.append(departure[1])

        return ans

# it passes the two example cases but results in 'runtime error' when a list is [["JFK","KUL"],["JFK","NRT"],["NRT",
# "JFK"]] why?


tick = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]


def find_itinerary(tickets):
    ans = []

    if len(tickets) == 0:
        return ans

    dep = find_earliest_ticket(tickets)


def find_earliest_ticket(tickets, departure_point=None):
    departure_list = []

    if departure_point is None:
        departure_point = "JFK"

    for ticket in tickets:
        if ticket[0] == departure_point:
            departure_list.append(ticket)

    return sorted(departure_list, key=lambda x: x[1])[:][0]

# can't figure out now... I'll keep on it tomorrow
# 29 AUG, let's give it another try
# tick = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# The reason has just been found. It doesn't have the next destination if ["JFK", "KUL"] is chosen
# It does have a smaller lexical order but ["JFK", NRT"] should be picked out for its own good

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []

        departure = self.find_earliest_ticket(tickets)
        ans.append(departure[0])
        tickets.remove(departure)

        while tickets:
            departure = self.find_earliest_ticket(tickets, departure[1])
            ans.append(departure[0])
            tickets.remove(departure)

        ans.append(departure[1])

        return ans

    def find_earliest_ticket(self, tickets, departure_point=None):
        departure_list = []

        if departure_point is None:
            departure_point = "JFK"

        for ticket in tickets:
            if ticket[0] == departure_point:
                departure_list.append(ticket)

        sorted_list = sorted(departure_list, key=lambda x: x[1])

        for i in range(len(sorted_list)):
            destination = sorted_list[i][1]

            for ticket in tickets:
                if ticket[0] == destination:
                    return sorted_list[i]
                elif len(tickets) == 1:
                    return ticket


"""
added some lines to pick an element only if ticket[1] exists as the next destination,
except only one element left in the ticket list

it passed the previous case but run into a new problem
: 'NoneType obejct is not subscriptable'

Also the time complexity increases to O(n^2)

Maybe it is time to refer to an explanation in the book and get some ideas to keep me going.
"""

# hint 1: create a graph with defalutdict(list), and search the data with dfs, the list should be sorted first
# as it should follow lexical order

import collections


def find_itinerary(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    # dep stands for departure
    def dfs(dep):
        while graph[dep]:
            route.append(dep)
            des = graph[dep].pop(0)
            dfs(des)

    dfs("JFK")

    return route
# the answer is ['JFK','SFO','ATL','JFK','ATL','SFO'] but what it gave me is ['JFK', 'ATL', 'JFK', 'SFO', 'ATL']

def find_itinerary(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    # dep stands for departure
    def dfs(dep):
        while graph[dep]:
            dfs(graph[dep].pop(0))
        route.append(dep)

    dfs("JFK")

"""
this works:

    def dfs(dep):
        while graph[dep]:
            dfs(graph[dep].pop(0))
        route.append(dep)

but why not this?

    def dfs(dep):
        while graph[dep]:
            route.append(dep)
            dfs(graph[dep].pop(0))

: now that a list have no element in the last loop, the last one is left out
    
by the way, I realised this line, des = graph[dep].pop(0), can be shortened to dfs(graph[dep].pop(0))
"""

# kind of got my head around the differences by drawing the process by myself
