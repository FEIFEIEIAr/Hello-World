# HYJ
# TIME: 2021-6-1 22:53


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('C:\\Users\\lanhao\\Desktop\\datas.xlsx',header = 0)

la = list(df.iloc[:,3])
lb = list(df.iloc[:,4])
journal = {}
keywords = {}
for i in la:
    journal[i] = journal.get(i,0) + 1 

plt.bar(list(journal.keys()),list(journal.values()),width = 0.5)
params = {'figure.figsize':'55,15'}
plt.rcParams.update(params)
plt.rcParams['figure.dpi'] = 100
plt.xticks(fontsize = 4)
plt.show()

df1=df.dropna(axis=0)
df1
lb = list(df1.iloc[:,4])
ls=[]
for a in lb:
    b = a.split(';')
    ls.append(b)
for x in ls:
    for y in x:
        keywords[y] = keywords.get(y,0)+1
plt.bar(list(keywords.keys()),list(keywords.values()),width = 0.5)
params = {'figure.figsize':'55,15'}
plt.rcParams.update(params)
plt.rcParams['figure.dpi'] = 100
plt.xticks(fontsize = 4)
plt.show()

