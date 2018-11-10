def indexed_search(items, element, index):
    return items[index] == element

list = [0, 1, 3, 6, 9, 11, 13, 17, 20, 28, 32, 34, 39, 42, 44, 48, 50, 55, 60, 70, 85]
found = indexed_search(list, 60, 18)
found