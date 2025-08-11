from random import randint
import timeit


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
for i in range(1000):
    arr.append(randint(0,10000))
print(arr)
rez = merg_sort(arr)
print(rez)

s = """def merg_sort_t():
        merg_sort(arr)
"""
print(timeit.timeit(stmt=s, number=100))
          #10                     100                          1000
#1.4100223779678345e-05   1.4099758118391037e-05   1.4600344002246857e-05
#1.4400109648704529e-05   1.4099758118391037e-05   1.5399884432554245e-05
#1.5799887478351593e-05   1.3899989426136017e-05   1.5200115740299225e-05
#1.4299992471933365e-05   1.4699995517730713e-05   1.5000347048044205e-05
#1.4800112694501877e-05   1.4099758118391037e-05   1.4500226825475693e-05



