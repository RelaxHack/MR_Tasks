import numpy as np
import csv

data = list(csv.reader(open("09_Irkutsk.csv")))
#p+1 номер месяца 
#i номер начальной строки
p = 3
i = 1
g = 0
x = []
y = []

while True:
    try:
        if float(data[i][p]) == 999.9:
            i += 1
            continue
        x.append(g)
        g += 1
        y.append(float(data[i][p]))
        i += 1
        if g > 13:
            break
    except IndexError:
        break
    
def lagranz1(x0):
    L = 0
    for j in range(len(y)):
        p=1
        for i in range(len(x)):
            if i != j:
                p *= (x0-x[i])/float(x[j]-x[i])
        L += y[j]*p
    return L
    
def lagranz(x0):
    L = 0
    for j in range(len(y)):
        p1=1
        p2=1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (x0-x[i])
                p2 = p2 * (x[j]-x[i])
        L = L + y[j]*p1/p2
    return L

xnew = []
ynew = []
for i in np.arange(1,len(y),0.1):
    if abs(lagranz1(i) - lagranz1(i+1)) > 100:
        continue
    xnew.append(i)
    ynew.append(lagranz1(i))

import matplotlib.pyplot as plt
plt.grid()
plt.plot(xnew,ynew)
