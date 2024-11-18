import pytest
from Sorts.Quick_u import quick_sort
from Sorts.Quick_v import quick_sort_ver

def test_sort():
    test_cases = [
        [1, 1, 2, 3, 3, 1],
        [5, 4, 3, 2, 1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [1, 1, 1, 1, 1],
        [],
        [0, 0, 0],
        [2, 1, 0, 1, 2]
    ]
    test_cases1 = [
        [1, 1, 1, 2, 3, 3],
        [1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 1, 1, 1, 1],
        [],
        [0, 0, 0],
        [0, 1, 1, 2, 2]
    ]
    for i in range(len(test_cases)):
        assert quick_sort(test_cases[i]) == test_cases1[i]
    #for i in range(len(test_cases)):
        #assert quick_sort_ver(test_cases[i]) == test_cases1[i]
