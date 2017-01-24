def insertion_sort(lst):
    for i in range(1, len(lst)):
        while i > 0 and lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst
lst = [int(x) for x in input().split()]
lst = insertion_sort(lst)
print(' '.join(str(x) for x in lst))
