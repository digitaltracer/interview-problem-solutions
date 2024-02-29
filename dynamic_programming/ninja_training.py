# Created by Adarsh N B at 1/9/2024

# Description:
"""
Ninja is planning n days long training schedule. Each day he can perform any of these 3 activities.
Each activity has some merit points on each day. As ninja has to improve all his skills , he can't do the same
activity in two consecutive days.
Find out the maximum merit points ninja can earn.

You are given 2D array of size n*3 points with the points corresponding to each day and activity.

Time complexity - 
Space complexity - 
"""
from typing import List
from copy import deepcopy


def ninja_training_rec(n: int, points: List[List[int]]) -> int:
    d2 = [-1] * 4
    dp = []
    for i in range(n):
        dp.append(deepcopy(d2))

    return ninja_training_rec_helper(points, n-1, 3, dp)


def ninja_training_rec_helper(points: List[List[int]], day: int, last_task: int, dp: List[List[int]]) -> int:

    if day == 0:
        day_0_max = max([i for ind, i in enumerate(points[0]) if last_task != ind])
        return day_0_max

    try:
        if dp[day][last_task] != -1:
            return dp[day][last_task]
    except Exception as e:
        print(day)
        print(last_task)
        raise e

    maximum_point = 0
    for task in range(3):
        if task != last_task:
            maximum_point = max(maximum_point,
                                points[day][task] + ninja_training_rec_helper(points, day-1, task, dp))

    dp[day][last_task] = maximum_point

    return dp[day][last_task]


def ninja_training_tab(n: int, points: List[List[int]]) -> int:

    d2 = [0]*4
    dp = []
    for i in range(n):
        dp.append(deepcopy(d2))

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    dp[day][last] = max(dp[day][last], points[day][task] + dp[day-1][task])

    return dp[n-1][3]


def ninja_training_tab2(n: int, points: List[List[int]]) -> int:

    d2 = [0]*3
    dp = []
    for i in range(n):
        dp.append(deepcopy(d2))

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])

    for day in range(1, n):
        for last in range(3):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    dp[day][last] = max(dp[day][last], points[day][task] + dp[day-1][task])

    return max(dp[n-1])


def ninja_training_tab_space_optimized(n: int, points: List[List[int]]) -> int:
    # The only change will be we won't be using entire dp array
    pass


if __name__ == "__main__":
    pts = [[5, 50, 10], [1, 100, 20], [10, 110, 100]]
    print(ninja_training_rec(3, pts))
    print(ninja_training_tab(3, pts))
    print(ninja_training_tab2(3, pts))
