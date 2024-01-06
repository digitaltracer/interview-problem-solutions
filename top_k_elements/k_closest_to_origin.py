# Created by Adarsh N B at 12/13/2023

# Description:
"""
Given a list of points on a plane, where the plane is a 2-D array with (x, y) coordinates, find the k closest points
to the origin (0,0). Here the distance is the euclidean distance sqrt(x**2 + y**2)

Time complexity -
Space complexity -
"""
import heapq
from math import sqrt
from typing import List


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x**2 + self.y**2)

    # Only lesser than is used in max-heap. And since it will be in a max heap, the logic is reversed (as python
    # supports only min-heap and this is the hack to convert it into max heap)
    def __lt__(self, other):
        return self.distance() > other.distance()

    def __str__(self):
        return '[{self.x}, {self.y}]'.format(self=self)


def k_closest(points: List[Point], k: int):
    points_max_heap = []

    for i in range(k):
        heapq.heappush(points_max_heap, points[i])

    for i in range(k, len(points)):
        if points[i].distance() < points_max_heap[0].distance():
            heapq.heappop(points_max_heap)
            heapq.heappush(points_max_heap, points[i])

    return list(points_max_heap)


# Function used to convert list to string
def lst_to_str(lst):
    out = "["
    for i in range(len(lst)-1):
        out += str(lst[i]) + ", "
    out += str(lst[len(lst)-1]) + "]"
    return out


def main():
    points_one = [Point(1, 3), Point(3, 4), Point(2, -1)]
    points_two = [Point(1, 3), Point(2, 4), Point(2, -1), Point(-2, 2),
                  Point(5, 3), Point(3, -2)]
    points_three = [Point(1, 3), Point(5, 3), Point(3, -2), Point(-2, 2)]
    points_four = [Point(2, -1), Point(-2, 2), Point(1, 3), Point(2, 4)]
    points_five = [Point(1, 3), Point(2, 4), Point(2, -1), Point(-2, 2),
                   Point(5, 3), Point(3, -2), Point(5, 3), Point(3, -2)]

    k_list = [2, 3, 1, 4, 5]
    points = [points_one, points_two, points_three, points_four, points_five]

    for i in range(len(k_list)):
        result = k_closest(points[i], k_list[i])
        print(i + 1, ".\tSet of points: ", sep="", end='')
        print(lst_to_str(points[i]))
        print("\tk:", k_list[i])
        print("\tHere are the k =", k_list[i], "points closest to the",
              "origin (0, 0): ", end='')
        print(lst_to_str(result))
        print("-"*100)


if __name__ == '__main__':
    main()
