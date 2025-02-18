import sys
def func(l):
    if len(l) < 3:
        sys.exit()
    else:
        m1 = max(l)
        m2 = min(l)
        return(m1-m2)


l = list(map(int,input().split()))
print("Range:",func(l))