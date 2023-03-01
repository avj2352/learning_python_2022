'''
Quick sort using Python
Space Time Complexity:
- Avg case: O(nlogn)
- Worse case: O(n^2)
- Space: O(2n)
'''
from typing import Union, List
Num = Union[int, float]

# quick sort algorithm
def quick_sort(arr: List[Num]) -> List[Num]:
    # base case
    if len(arr) <= 1:
        return arr

    # find pivot
    pivot = arr[len(arr) - 1]
    # define lists
    left, right = [], []
    # iterate
    for el in range(0, len(arr)-1):
        left.append(arr[el]) if arr[el] < pivot else right.append(arr[el])
    # recurse
    return [*quick_sort(left), pivot, *quick_sort(right)]

# TESTING
input_list = [5,4,10,3,7,9,1,2,6,30]
print(f"Quick sort algorithm of {input_list} is: {quick_sort(input_list)}")
