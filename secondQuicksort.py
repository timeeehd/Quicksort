'''
Dual Pivot Quicksort with Yaroslavskiy's partitioning method
'''
# import math
# import random
# from typing import List
# from utility import *


def dual_pivot_quicksort(array, left, right):
    if (right - left >= 1):
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]
        pivot = array[left]
        quivot = array[right]
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


# def generate_input(n: int) -> List[int]:
#     return [i for i in range(1, n + 1)]
#
#
# def generate_negative_input(n: int) -> List[int]:
#     return [i for i in range(0, -n, -1)]
#
#
# def generate_equal_input(n: int) -> List[int]:
#     return [n for i in range(1, n + 1)]
#
#
# def generate_random_input(n: int) -> List[int]:
#     list = []
#     for i in range(n):
#         random_int = random.randint(1, int(math.sqrt(n)))
#         list.append(random_int)
#     return list


# if __name__ == '__main__':
#     max_i: int = 5
#     N: int = 5
#     # random shuffled list
#     ns = [int(30 * 1.41 ** i) for i in range(max_i)]
#     args = [generate_input(n) for n in ns]
#     for sublist in args:
#         random.shuffle(sublist)
#     print(args)
#     for sublist in args:
#         sorted_list = sort_func(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
#
#     # reversed sorted list
#     reversed_args = [generate_input(n) for n in ns]
#     for sublist in reversed_args:
#         sublist.reverse()
#     print(reversed_args)
#     for sublist in reversed_args:
#         sorted_list = sort_func(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
#
#     # negative integer list
#     negative_list = [generate_negative_input(n) for n in ns]
#     print(negative_list)
#     for sublist in negative_list:
#         sorted_list = sort_func(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
#
#
#     equal_list = [generate_equal_input(n) for n in ns]
#     print(equal_list)
#     for sublist in equal_list:
#         sorted_list = sort_func(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
#
#
#     random_list = [generate_random_input(n) for n in ns]
#     print(random_list)
#     for sublist in random_list:
#         sorted_list = sort_func(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
