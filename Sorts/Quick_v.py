import random

def quick_sort_ver(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop(random.randint(0, len(arr) - 1))
    les_p = []
    great_p = []
    for elem in arr:
        if elem >= pivot:
            great_p.append(elem)
        else:
            les_p.append(elem)
    return quick_sort_ver(les_p) + [pivot] + quick_sort_ver(great_p)