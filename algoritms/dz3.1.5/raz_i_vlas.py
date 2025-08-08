from random import randint

def merg_sort(arr):
    if len(arr) > 1:
        mid = len(arr) //2
        left_half = arr[:mid]
        rigt_half = arr[mid:]

        merg_sort(left_half)
        merg_sort(rigt_half)

        i = j = k = 0
        while i < len(left_half) and j < len(rigt_half):
            if left_half[i] < rigt_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = rigt_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i +=1
            k += 1
        while j < len(rigt_half):
            arr[k] = rigt_half[j]
            j += 1
            k += 1
        return arr

arr = []
for i in range(10):
    arr.append(randint(0,100))
print(arr)
rez = merg_sort(arr)
print(rez)
print("свмый большой элемент в списке:", rez[-1])