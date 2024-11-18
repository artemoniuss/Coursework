def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop(int(len(arr) / 2))
    les_p = []
    great_p = []
    for elem in arr:
        if elem >= pivot:
            great_p.append(elem)
        else:
            les_p.append(elem)
    return quick_sort(les_p) + [pivot] + quick_sort(great_p)