from random import randint

def sum_list(arr):
    if not arr:
        return 0
    elif len(arr) <= 1:
        return arr[0]

    else:
        return arr[0] + sum_list(arr[1:])



arr = []
for i in range(10):
    arr.append(randint(0,100))
print(arr)


print(sum_list(arr))

