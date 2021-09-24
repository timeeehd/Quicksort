import copy


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


if __name__ == '__main__':
    # test = [7,6,5,4,3,2,1]
    test = [2, 3, 1, 4, 6, 7, 5]
    # test = [1, 2, 3, 4, 5, 6, 7]
    sorted_list = quick_sort_add_sent(test, 0, len(test) - 1)
    print(sorted_list)
