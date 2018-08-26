# Binary search uses for ordered sequences

def binatySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first<=last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

# testlist = [1, 3, 5, 7, 12, 15, 19, 23]
# print(binatySearch(testlist, 4))
# print (binatySearch(testlist, 19))


# Recursive version

