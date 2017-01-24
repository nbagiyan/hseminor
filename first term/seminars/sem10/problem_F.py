def SelectionSort (A):
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] > A[i]:
                 A[i], A[j] = A[j], A[i]
    return A

lst = [int(x) for x in input().split()]
print(' '.join(str(x) for x in SelectionSort(lst)))
