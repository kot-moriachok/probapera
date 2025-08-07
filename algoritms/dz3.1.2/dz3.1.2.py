import random
import timeit

def spisok():
    # Создаем список из 100 случайных чисел (например, от  до 999)
    random_numbers = [random.randint(0, 9999) for _ in range(100)]
    #print(random_numbers)
    spisok_sort = sorted(random_numbers)
    #print(spisok_sort)
    num = s #int(input("введите число для поиска "))

    ferst = 0
    mid = len(spisok_sort) // 2
    last = len(spisok_sort) - 1

    while spisok_sort[mid] != num and ferst <= last:
        if num > spisok_sort[mid]:
            ferst = mid + 1
        else:
            last = mid -1
        mid = (ferst + last) // 2

    if ferst > last:
        print("Такого числа нет")
    else:
        print("Индекс числа:" , mid)

s = int(input("введите число для поиска "))
print(timeit.timeit(spisok, number=100))



