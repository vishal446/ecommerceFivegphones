from fractions import Fraction
from functools import reduce
# l=[]
# for _ in range(int(input())):
#     l.append(*map(int,input().split()))
# for i in l:
#     print(list(l))S
# l=[1/3,2/4,3/6]
# t=reduce(lambda x,y:x*y,l)
# print(t)
from itertools import combinations
s='HACK 2'
t=list(combinations(s,2))
l=[]
p=[]
for i in t:
    c=''
    for j in i:
        c=c+j
        l.append(c)     
d=set(l)
print(d)