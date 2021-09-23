import copy


def quicksort(array, left, right):
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
                j = j - 1
                mem = array[j]
                if mem <= p:
                    break
            if j > i:
                memory = copy.deepcopy(array)
                array[i] = memory[j]
                array[j] = memory[i]
            elif i > j:
                break
        memory = copy.deepcopy(array)
        array[i] = memory[right]
        array[right] = memory[i]
        # array.pop(0)
        # left = left - 1
        array[left:i] = quicksort(array, left, i - 1)[left:i]
        array[i + 1:] = quicksort(array, i + 1, right)[i + 1:]
        return array
    else:
        return array


def sort_func(array, left, right):
    array = [-1000000] + array
    sorted_list = quicksort(array, left + 1, right + 1)
    sorted_list.pop(0)
    return sorted_list


if __name__ == '__main__':
    test = [7,6,5,4,3,2,1]
    sorted_list = sort_func(test, 0, len(test) - 1)
    print(sorted_list)
