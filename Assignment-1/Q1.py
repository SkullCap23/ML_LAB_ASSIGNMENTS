def find_pairs(l):
    L = []
    l = sorted(l)
    i = 0
    j = len(l) - 1
    while i < j:
        csum = l[i] + l[j]
        if csum > 10:
            j = j - 1
        elif csum < 10:
            i = i + 1
        else:
            L.append([l[i], l[j]])
            i += 1
            j -= 1
    return L


l = list(map(int, input().split()))
print(find_pairs(l))
