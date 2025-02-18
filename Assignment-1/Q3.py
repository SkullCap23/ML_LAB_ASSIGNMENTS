import numpy as np
from numpy.linalg import matrix_power

def func(m,r):
    M = []
    for i in range(r):
        l = list(map(int,input().split()))
        M.append(l)
    return matrix_power(M,m)

m = int(input("enter power: "))
r = int(input("enter # of rows: "))
print(func(m,r))