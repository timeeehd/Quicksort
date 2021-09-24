'''
Dual Pivot Quicksort with Yaroslavskiy's partitioning method
'''
import random
from typing import List


def dual_pivot_quicksort(array, left, right):
    if (right - left >= 1):
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]
        pivot = array[left]
        quivot = array[right]
        #if pivot > quivot:
            # swap p and q
        #    pivot, quivot = quivot, pivot
        l = left + 1
        g = right - 1
        k = l

        while (k <= g):
            if (array[k] < pivot):
                # Swap element
                array[k], array[l] = array[l], array[k]
                l = l + 1
            else:
                if (array[k] > quivot):
                    while (array[g] > quivot and k < g):
                        g = g - 1
                    # swap element
                    array[k], array[g] = array[g], array[k]
                    g = g - 1
                    if (array[k] < pivot):
                        array[k], array[l] = array[l], array[k]
                        l = l + 1
            k = k + 1

        l = l - 1
        g = g + 1

        # Swap A[left] A[l] bring pivot to final position
        array[left], array[l] = array[l], array[left]
        # Swap A[right] A[g]
        array[right], array[g] = array[g], array[right]
        dual_pivot_quicksort(array, left, l - 1)
        dual_pivot_quicksort(array, l + 1, g - 1)
        dual_pivot_quicksort(array, g + 1, right)
    return array

def sort_func(array, left, right):
    array = [-1000000] + array
    sorted_list = dual_pivot_quicksort(array, left + 1, right + 1)
    sorted_list.pop(0)
    return sorted_list

def generate_input(n: int) -> List[int]:
    return [i for i in range(1, n + 1)]

if __name__ == '__main__':
    max_i: int = 12
    N: int = 5
    ns = [int(30 * 1.41 ** i) for i in range(max_i)]
    args = [generate_input(n) for n in ns]
    for ar in args:
        random.shuffle(ar)
    print(args)
    for ar in args:
        sorted_list = dual_pivot_quicksort(ar, 0, len(ar)-1)
        print(sorted_list)


