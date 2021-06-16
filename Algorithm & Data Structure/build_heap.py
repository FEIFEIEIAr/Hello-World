# python3
from math import floor
def shift(i):
    index = i
    l = 2*i + 1
    r = l + 1
    if l+1 <= len(data) and data[l] < data[index]:
        index = l
    if r+1 <= len(data) and data[r] < data[index]:
        index = r
    if i != index:
        data[i], data[index] = data[index], data[i]
        swaps.append((i, index))
        shift(index)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    flag = len(data)
    for i in range(0, len(data)):
        n = flag - i - 1
        shift(n)


if True:
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = []

    build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

