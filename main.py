from Sorts.Counter import Counter_time
import random

if __name__ == "__main__":
    choices = {
        1: "Сравнить время работы",
        2: "Задать новую последовательность чисел",
        3: "Выход из программы"
    }
    mass_for_sort = []
    num_cou1 = int(input("Задайте количество элементов массива: "))
    num_val1 = int(input("Задайте верхнюю границу числа: "))
    for i in range(num_cou1):
        mass_for_sort.append(random.randint(0, num_val1))
    while True:
        for key, value in choices.items():
            print(f"{key}. {value}")
        choice = int(input("Ваш выбор: "))
        if choice not in choices:
            print("Неправильный выбор. Пожалуйста, выберите один из доступных вариантов.")
            continue
        if choice == 1:
            Counter_time.comparsion(mass_for_sort)
        if choice ==  2:
            mass_for_sort.clear()
            num_cou = int(input("Задайте количество элементов массива: "))
            num_val = int(input("Задайте верхнюю границу числа: "))
            for i in range(num_cou):
                mass_for_sort.append(random.randint(0, num_val))
        if choice ==  3:
            print("До свидания!!!")
            break