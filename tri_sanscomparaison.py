# -*- coding: utf-8 -*-

import random

N = 100

tab = []

for i in range (0,N-1) :
  tab.append(random.randint(0,N-1))
 
tri = [-1]*N
doublon = []

for i in range (0,N-1) :
    j = tab[i]
    if tri[j-1] == -1 :
        tri[j-1] = j
    else :
        doublon.append(j)

h = tri.count(-1) 
for i in range (0,h) :       
    tri.remove(-1)

n = len(doublon)

for i in range (0,n-1) :
    j = tri.index(doublon[i])
    tri.insert(j,doublon[i])
    
print (tri)