'''
pytest execute with "pytest ." or "pytest test_quicksort.py"
'''

import firstQuicksort, secondQuicksort



simpleSortList = [1, 5, 2]
sortWithNegativeList = [1, 2, -3, 4]

#incompleteTestList = [2,-2]
emptyTestList = []

equalIntegerTestList = [1, 2, 2, 1, 3, 3]
distinctReverseList = [5, 4, 3, 2, 1]


def test_always_passes():
    assert True


# def test_always_fails():
#    assert False

# Test for cubic
def test_simple_list():
    assert firstQuicksort.quick_sort_no_sent(simpleSortList, 0, len(simpleSortList) -1) == sorted(simpleSortList)
    assert secondQuicksort.dual_pivot_quicksort(simpleSortList, 0, len(simpleSortList) -1) == sorted(simpleSortList)

def test_with_negative():
    assert firstQuicksort.quick_sort_no_sent(sortWithNegativeList, 0, len(sortWithNegativeList) - 1) == sorted(sortWithNegativeList)
    assert secondQuicksort.dual_pivot_quicksort(sortWithNegativeList, 0, len(sortWithNegativeList) - 1) == sorted(sortWithNegativeList)


def test_empty_list():
    assert firstQuicksort.quick_sort_no_sent(emptyTestList, 0,len(emptyTestList) - 1) == []
    assert secondQuicksort.dual_pivot_quicksort(emptyTestList, 0,len(emptyTestList) - 1) == []


def test_equal_integer():
    assert firstQuicksort.quick_sort_no_sent(equalIntegerTestList, 0,len(equalIntegerTestList) - 1) == sorted(equalIntegerTestList)
    assert secondQuicksort.dual_pivot_quicksort(equalIntegerTestList, 0,len(equalIntegerTestList) - 1) == sorted(equalIntegerTestList)

def distinct_reverse_list():
    assert firstQuicksort.quick_sort_no_sent(distinctReverseList, 0,len(distinctReverseList) - 1) == sorted(distinctReverseList)
    assert secondQuicksort.dual_pivot_quicksort(distinctReverseList, 0,len(distinctReverseList) - 1) == sorted(distinctReverseList)


# TODO: write more/meaningful test cases

