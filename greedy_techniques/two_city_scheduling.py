# Created by Adarsh N B at 11/23/2023

# Description:
"""
A recruiter plans to hire n people and conducts their interviews at two different locations of the company.
He evaluates the cost of inviting candidates to both these locations. The plan is to invite 50% at one location, and
the rest at the other location, keeping costs to a minimum. We are given an array, costs, where
costs[i]=[aCost[i], b[Cost[i]], the cost of inviting the ith person to City A is aCosti, and the cost of inviting the
same person to City B is bCosti.
You need to determine the minimum cost to invite all the candidates for the interview such that exactly n/2
people are invited in each city.

Time complexity - O(nlogn)  (Since we are sorting the array first)
Space complexity - O(n)  (Sorting the array takes O(n) space in python)
"""


def two_city_scheduling(costs):
    total_cost = 0
    costs.sort(key=lambda x: x[0] - x[1])
    half_index = len(costs)//2
    for cost in costs[:half_index]:
        total_cost += cost[0]
    for cost in costs[half_index:]:
        total_cost += cost[1]
    return total_cost
