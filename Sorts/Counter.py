from Sorts.Quick_u import quick_sort
from Sorts.Quick_v import quick_sort_ver
import time

class Counter_time:
    def comparsion(arr):
        start_time1 = time.time()
        sorted_arr1 = quick_sort(arr)
        end_time1 = time.time()
        execution_time1 = end_time1 - start_time1
        start_time2 = time.time()
        sorted_arr2 = quick_sort_ver(arr)
        end_time2 = time.time()
        execution_time2 = end_time2 - start_time2
        print(f"Отсортированный массив быстрой сортировкой: {sorted_arr1}")
        print(f"Время выполнения быстрой сортировки: {execution_time1} секунд")
        print(f"Отсортированный массив вероятностной быстрой сортировкой: {sorted_arr2}")
        print(f"Время выполнения вероятностной быстрой сортировки: {execution_time2} секунд")