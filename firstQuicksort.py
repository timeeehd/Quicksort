import random


def quicksort_sent(array, left, right):
    # left = left + 1
    if right - left >= 1:
        # array = [-1000000] + array
        # right most element as pivot
        p = array[right]
        i = left - 1
        j = right
        while True:
            while True:
                i = i + 1
                mem = array[i]
                if mem >= p:
                    break
            while True:
                # When removing the sentinel, with python, it still seems to be working fine, bc in python
                # when j goes negative, it just takes the last element, which in this case is the pivot itself
                j = j - 1
                mem = array[j]
                if mem <= p:
                    break
            if j > i:
                array[i], array[j] = array[j], array[i]
            elif i > j:
                break
        array[i], array[right] = array[right], array[i]
        # array.pop(0)
        # left = left - 1
        quicksort_sent(array, left, i - 1)[left:i]
        quicksort_sent(array, i + 1, right)[i + 1:]
    return array


def quick_sort_add_sent(array, left, right):
    array = [-1000000] + array
    sorted_list = quicksort_sent(array, left + 1, right + 1)
    sorted_list.pop(0)
    return sorted_list


def quick_sort_no_sent(array, left, right):
    # left = left + 1
    if right - left >= 1:
        # array = [-1000000] + array
        # right most element as pivot
        p = array[right]
        i = left - 1
        j = right
        while True:
            while True:
                i = i + 1
                mem = array[i]
                if mem >= p:
                    break
            while True:
                # When removing the sentinel, with python, it still seems to be working fine, bc in python
                # when j goes negative, it just takes the last element, which in this case is the pivot itself
                j = j - 1
                mem = array[j]
                if mem <= p:
                    break
            if j > i:
                array[i], array[j] = array[j], array[i]
            elif i > j:
                break
        array[i], array[right] = array[right], array[i]
        # array.pop(0)
        # left = left - 1
        quicksort_sent(array, left, i - 1)[left:i]
        quicksort_sent(array, i + 1, right)[i + 1:]
    return array


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
#         sorted_list = quick_sort_add_sent(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
#
#     # reversed sorted list
#     reversed_args = [generate_input(n) for n in ns]
#     for sublist in reversed_args:
#         sublist.reverse()
#     print(reversed_args)
#     for sublist in reversed_args:
#         sorted_list = quick_sort_add_sent(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
#
#     # negative integer list
#     negative_list = [generate_negative_input(n) for n in ns]
#     print(negative_list)
#     for sublist in negative_list:
#         sorted_list = quick_sort_add_sent(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
#
#
#     equal_list = [generate_equal_input(n) for n in ns]
#     print(equal_list)
#     for sublist in equal_list:
#         sorted_list = quick_sort_add_sent(sublist, 0, len(sublist) - 1)
#         print(sorted_list)
#
#
#     random_list = [generate_random_input(n) for n in ns]
#     print(random_list)
#     for sublist in random_list:
#         sorted_list = quick_sort_add_sent(sublist, 0, len(sublist) - 1)
#         print(sorted_list)