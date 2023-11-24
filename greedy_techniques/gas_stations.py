# Created by Adarsh N B at 11/23/2023

# Description:
"""
There are n gas stations along a circular route, where the amount of gas at the `ith` station is `gas[i]`.

We have a car with an unlimited gas tank, and it costs `cost[i]` of gas to travel from the `ith` station to the next
`(i+1)th` station. We begin the journey with an empty tank at one of the gas stations.

Find the index of the gas station in the integer array `gas` such that if we start from that index we may return to the
same index by traversing through all the elements, collecting `gas[i]` and consuming `cost[i]`.

If it is not possible, return -1.

If there exists such index, it is guaranteed to be unique.
"""
from typing import List


def gas_station_journey(gas_stations: List[int], costs: List[int]) -> int:

    start_index = current_gas = 0

    if sum(costs) > sum(gas_stations):
        return -1

    for i in range(len(gas_stations)):
        current_gas = current_gas + (gas_stations[i] - costs[i])

        if current_gas < 0:
            current_gas = 0
            start_index = i + 1

    return start_index


def main():
    gas = [[1, 2, 3, 4, 5], [2, 3, 4], [1, 1, 1, 1, 1], [
        1, 1, 1, 1, 10], [1, 1, 1, 1, 1], [1, 2, 3, 4, 5]]
    cost = [[3, 4, 5, 1, 2], [3, 4, 3], [1, 2, 3, 4, 5], [
        2, 2, 1, 3, 1], [1, 0, 1, 2, 3], [1, 2, 3, 4, 5]]
    for i in range(len(gas)):
        print(i+1, ".\tGas = ", gas[i], sep="")
        print("\tCost = ", cost[i])
        print("\n \tThe index of the gas station we can start our journey from is ", gas_station_journey(
            gas[i], cost[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
