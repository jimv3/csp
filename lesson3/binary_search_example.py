def binary_search(items, element):
    found = False
    low = 0
    high = len(items)
    while low < high and not found:
        middle = (high+low)//2-1
        if items[middle] == element:
            found = True
        elif items[middle] < element:
            low = middle+1
        else:
            high = middle-1
    return found


list = [0, 1, 3, 6, 9, 11, 13, 17, 20, 28, 32,
        34, 39, 42, 44, 48, 50, 55, 60, 70, 85]
found = binary_search(list, 60)
found
