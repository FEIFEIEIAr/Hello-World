# HYJ
# TIME: 2021-6-10 23:03
from math import floor
from math import log2
import random


# a binary tree, using mathematics relation between node and it's child and parent
class BHeap:
    def __init__(self, tree=None):
        self.tree = tree
        self.Rebuild()

    def Size(self):
        return len(self.tree)

    def Self(self,i):
        return self.tree[i - 1]

    def Parent(self, i):
        if i == 1:
            return print('root does not have parent')
        return self.tree[floor(i / 2) - 1]

    def LeftChild(self, i):
        return self.tree[2 * i - 1]

    def RightChild(self, i):
        return self.tree[2 * i]

    def ParentIndex(self, i):
        if i == 1:
            return print('root does not have parent')
        return floor(i/2)

    def LeftChildIndex(self, i):
        return 2*i

    def RightChildIndex(self, i):
        return 2*i + 1

    def ShiftUp(self, i):
        if i > 1 and self.Parent(i) < self.Self(i):
            self.tree[i-1], self.tree[floor(i/2)-1] = self.tree[floor(i/2)-1], self.tree[i-1]
            i = floor(i/2)
            self.ShiftUp(i)

    def ShiftDown(self, i):
        flag = i
        if self.LeftChildIndex(i) <= self.Size() and self.LeftChild(i) > self.Self(flag):
            flag = self.LeftChildIndex(i)

        if self.RightChildIndex(i) <= self.Size() and self.RightChild(i) > self.Self(flag):
            flag = self.RightChildIndex(i)

        if i != flag:
            self.tree[i-1], self.tree[flag - 1] = self.tree[flag - 1], self.tree[i-1]
            self.ShiftDown(flag)

    def Insert(self, item):
        self.tree.append(item)
        self.ShiftUp(self.Size())

    def ExtractMax(self):
        result = self.tree[0]
        self.tree[0] = self.tree[self.Size()-1]
        self.tree.pop()
        self.ShiftDown(1)
        if result == float('inf'):
            return
        else:
            print('Max is {0}, and it has been extracted out'.format(result))
            return result

    def Remove(self, i):
        self.tree[i - 1] = float('inf')
        self.ShiftUp(i)
        self.ExtractMax()

    def ChangePriority(self, i, item):
        old_item = self.Self(i)
        self.tree[i-1] = item
        if old_item <= item:
            self.ShiftUp(i)
        else:
            self.ShiftDown(i)

    def Show(self):
        print(self.tree)

    def Height(self):
        n = len(self.tree)
        if n == 1:
            k = 1
        else:
            k = floor(log2(n))+1
        print('Tree\'s height is {0}'.format(k))

    def HeapSort(self):
        size = len(self.tree)
        lst = []
        if size == 1:
            return self.Show()
        else:
            for i in range(size):
                self.tree[0], self.tree[size-1] = self.tree[size-1], self.tree[0]
                size -= 1
                x = self.tree.pop()
                self.ShiftDown(1)
                lst.insert(0, x)
            self.tree = lst
        return print("It's now {0}, but it's no longer a heap, and you can do rebuild to make it a heap again".format(lst))

    def Rebuild(self):
        """for i, item in enumerate(self.tree):
            self.ShiftUp(i+1)"""
        size = len(self.tree)
        size = floor(size)
        flag = size
        for i in range(size):
            self.ShiftDown(flag)
            flag -= 1


lens = random.randint(1, 20)
lst = []
for i in range(lens):
    lst.append(random.randint(0, 100))

"""lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""
t = BHeap(lst)
t.Remove(5)
t.Insert(1000)
t.ExtractMax()
t.ChangePriority(1, 5)
t.Height()
t.Show()
t.HeapSort()
t.Rebuild()
t.Show()
