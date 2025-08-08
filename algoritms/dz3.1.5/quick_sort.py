from random import randint
import timeit

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = []
for i in range(1000):
    arr.append(randint(0,10000))
print(arr)

print(quick_sort(arr))

s = """def quick_s():
        spisok(arr)
"""
print(timeit.timeit(stmt=s, number=100))

#заиеры времени для 10
#  1.4199875295162201e-05
#  1.400010660290718e-05
#  1.4299992471933365e-05
#  1.4800112694501877e-05
#  1.4199875295162201e-05
# Для 100
#  1.4400109648704529e-05
#  1.4899764209985733e-05
#  1.4899764209985733e-05
# для 1000
#  1.5900004655122757e-05
#  1.5700235962867737e-05
#  1.4699995517730713e-05
# Вывод замеры практически не отличаются