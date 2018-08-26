def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


testlist = [1, 3, 7, 4, 7, 2, 9, 10]
print(sequentialSearch(testlist, 5))
print(sequentialSearch(testlist, 10))