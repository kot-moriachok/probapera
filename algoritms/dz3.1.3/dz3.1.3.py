from random import randint
import timeit

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swaped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swaped = True
        if not swaped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = []
for i in range(1000):
    arr.append(randint(0,9999))

print(arr)
print(bubble_sort(arr))
print(selection_sort(arr))
b = """def bubble_sort_t():
    bubble_sort(arr)
"""

s = """def selection_sort_t():
        selection_sort(arr)
"""
print(timeit.timeit(stmt=b, number=100))
print(timeit.timeit(stmt=s, number=100))


