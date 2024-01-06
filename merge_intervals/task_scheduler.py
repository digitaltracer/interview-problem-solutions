# Created by Adarsh N B at 11/30/2023

# Description:
"""

"""
from typing import List


def least_time(tasks: List[str], n: int) -> int:

    frequencies = {}

    for char in tasks:
        frequencies[char] = frequencies.get(char, 0) + 1

    # sort the dict based on the frequency of the letter
    frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1]))
    max_freq = frequencies.popitem()[1]
    idle_time = (max_freq - 1) * n

    while frequencies and idle_time > 0:
        idle_time -= min(max_freq - 1, frequencies.popitem()[1])
    idle_time = max(0, idle_time)

    return len(tasks) + idle_time


def main():
    all_tasks = [['A', 'A', 'B', 'B'],
                  ['A', 'A', 'A', 'B', 'B', 'C', 'C'],
                  ['S', 'I', 'V', 'U', 'W', 'D', 'U', 'X'],
                  ['M', 'A', 'B', 'M', 'A', 'A', 'Y', 'B', 'M'],
                  ['A', 'K', 'X', 'M', 'W', 'D', 'X', 'B', 'D', 'C', 'O', 'Z', 'D', 'E', 'Q']]
    all_ns = [2, 1, 0, 3, 3]

    for i in range(len(all_tasks)):
        print(i+1, '.', '\tTasks: ', all_tasks[i], sep='')
        print('\tn: ', all_ns[i], sep='')
        min_time = least_time(all_tasks[i], all_ns[i])
        print('\tMinimum time required to execute the tasks: ', min_time)
        print('-' * 100)


if __name__ == '__main__':
    main()
