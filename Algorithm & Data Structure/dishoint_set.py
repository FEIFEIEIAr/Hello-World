# HYJ
# TIME: 2021-6-15 22:30

class DisjointSet():
    def __init__(self, set=[], rank=[]):
        self.set = set
        self.rank = rank

    def MakeSet(self, i):
        while i >= len(self.set):
            self.set.append('null')
            self.rank.append('null')
        self.set[i] = i
        self.rank[i] = 0

    def Find(self, i):
        while i != self.set[i]:
            i = self.set[i]
        return i

    def Union(self, i, j):
        i_id = self.Find(i)
        j_id = self.Find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.set[j_id] = i_id
        else:
            self.set[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[j_id]+1

    def Show(self):
        print("", self.set, "\n", self.rank)


lst = DisjointSet()
for i in range(1, 13):
    lst.MakeSet(i)
lst.Union(2, 10)
lst.Union(7, 5)
lst.Union(6, 1)
lst.Union(3, 4)
lst.Union(5, 11)
lst.Union(7, 8)
lst.Union(7, 3)
lst.Union(12, 2)
lst.Union(9, 6)
lst.Show()

