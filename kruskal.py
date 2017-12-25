import random
import numpy as np
import matplotlib.pyplot as plt
import dataKruskal

def Euclidean(x,y):
    return np.sqrt(np.sum((x-y)**2))

#ДСУ - нам нужно определять в разных ли кластерах (компонентах) лежат вершины текущего ребра
class DSU:
    def __init__(self, n):
        self.n = n
        self.p = np.ones(n, dtype=int) * -1
    def Get(self, x):
        if self.p[x] == -1: return x
        self.p[x] = self.Get(self.p[x])
        return self.p[x]
    def Union(self, a, b):
        a = self.Get(a)
        b = self.Get(b)
        if a == b: return
        self.p[a] = b

#метод принимает выборку, кол-во кластеров, нужно ли отрисовать график, метрику
def Kruskal(X, needclasses, plotGraph=False, ro=Euclidean):
    l = X.shape[0]
    edges = []
    for i in range(l):
        for j in range(i+1,l):
            edges.append((ro(X[i],X[j]), i, j))
    edges = sorted(edges, key=lambda x: x[0])

    union = DSU(l)
    classes = l
    now = 0
    costs = []
    nclasses=[]
    while classes > needclasses:
        a = edges[now][1]
        b = edges[now][2]
        if union.Get(a) != union.Get(b):
            costs.append(edges[now][0])
            nclasses.append(classes-1)
            union.Union(a, b)
            classes -= 1
        now += 1

    # формируем кластеры
    # перенумеруем их в 0,1...
    dict = {}
    classes = 0
    for i in range(l):
        now = union.Get(i)
        if now not in dict:
            dict[now] = classes
            classes += 1

    # получаем из ДСУ класс
    y = np.zeros(l)
    for i in range(l):
        now = union.Get(i)
        y[i] = dict[now]
        
    if plotGraph:
        plt.xlabel('count classes')
        plt.ylabel('edge cost')
        plt.plot(nclasses, costs)
        plt.show()
        
    return y

X = dataKruskal.DataBuilder().Build("nice")
y = Kruskal(X,9,True)

colors=['red','green','blue','pink','purple','yellow','brown','black','gray'] 
ncolor=[] 
for i in range(len(y)): 
    pos = int(y[i]) 
    ncolor.append(colors[pos])
    
plt.scatter(X[:,0],X[:,1], c=ncolor)
plt.show()
