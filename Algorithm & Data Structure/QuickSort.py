import time
import random


def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        a = A[p]
        A[p] = A[q]
        A[q] = a
        QuickSort(A, p, q - 1)
        QuickSort(A, q+1, r)


def Partition(arr, low, high):
    x = arr[low]
    i = low
    j = high
    while True:
        while arr[j] > x and j >= low:
            j -= 1
        while arr[i] <= x and i < high:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break

    return j


start = time.time()

lst = []
for i in range(20):
    lst.append(random.randint(1, 100))
print(lst)
n = len(lst)
m = 0
QuickSort(lst, m, n-1)
print(lst)

end = time.time()
print(end - start)
## [46, 14, 1, 63, 34, 52, 85, 16, 77, 40]失败[3, 59, 6, 79, 93, 18, 50, 5, 47, 62]