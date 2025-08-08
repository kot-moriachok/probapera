from random import randint

def binary_serch_recursive(arr, low, higt, key):
    if low < higt:
        mid = (low + higt) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_serch_recursive(arr, mid + 1 ,higt, key)
        else:
            return binary_serch_recursive(arr, low, mid-1,key)
    else:
        return -1

arr = []
for i in range(10):
    arr.append(randint(0,100))
key = randint(0,100)
print(arr)
print(key)


print(binary_serch_recursive(arr,0,len(arr),key))