def func(s):
    m = 0
    a = None
    for i in s:
        if s.count(i) > m:
            m = s.count(i)
            a = i
    return a,m


s = input("enter string: ")
a,m = func(s)
print("The most frequent character is ",a,", occurring a total of ",m," times",sep='')