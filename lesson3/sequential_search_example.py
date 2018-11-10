def sequential_search(items, element):
    for n in items:
        if n == element:
            return True
    return False


list = [0, 1, 3, 6, 9, 11, 13, 17, 20, 28, 32,
        34, 39, 42, 44, 48, 50, 55, 60, 70, 85]
found = sequential_search(list, 60)
found
