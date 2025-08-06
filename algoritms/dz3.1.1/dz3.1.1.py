import random
import timeit

# Создаем список из 100 случайных чисел (например, от  до 999)
random_numbers = [random.randint(0, 9999) for _ in range(1000)]
print(random_numbers)
n = len(random_numbers)
key = 54
def spisok(random_numbers, n, key):
    for i in range(0, n):
        if random_numbers[i] == key:
            return i
    return -1

s = """def spisok_test():
        spisok(random_numbers, n, key)
"""
print(timeit.timeit(stmt=s, number=100))





