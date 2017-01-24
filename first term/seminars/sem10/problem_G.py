def merge(A, B):
    Res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            Res.append(A[i])
            i += 1
        else:
            Res.append(B[j])
            j += 1
    Res += A[i:] + B[j:]
    return Res

lst = [int(x) for x in input().split()]
lst1 = [int(x) for x in input().split()]
print(' '.join(str(x) for x in merge(lst, lst1)))
