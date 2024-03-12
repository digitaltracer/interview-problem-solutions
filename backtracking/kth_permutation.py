# Created by Adarsh N B at 3/5/2024

# Description:
"""
This is a recursion problem and not a backtracking problem
The set [1, 2, 3, 4, ... n] contains a total of n! unique permutations.
By listing and labeling all the permutations in order, we get the following sequence for n = 3
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k return the kth permutation sequence.

The bruteforce approach is to recursively generate all the permutations and then sort and then return the k-1th item.
But this takes O(n!*n) + O(n!logn!) which isn't ideal.

So, if you take an example of [1, 2, 3, 4] and k = 17, if you look at the pattern
starting with 1 + (2, 3, 4) you get 6 different permutations.
so on with starting with 2, 3, 4. So if you are looking for a 17th permutation,
you can generalise it to 17//6 + 17%6 => 5th permutation starting with 3.

To find the 5th permutation you can carry on the same logic recursively.

Which we can generalise further into k//(n-1)! starting digit and k%(n-1)! th permutation


Time complexity - 
Space complexity - 
"""
from typing import List


def kth_permutation(n: int, k: int) -> int:
    pass
