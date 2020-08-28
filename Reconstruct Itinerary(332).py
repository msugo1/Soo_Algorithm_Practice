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
