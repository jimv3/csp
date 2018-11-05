def bubble_sort_example(items):
    k = 0
    exchange_made = True
    n = len(items)
    while k < n and exchange_made:
        exchange_made = False
        k += 1
        for j in range(n - k):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                exchange_made = True
    return items


if 'unsorted_list' not in vars():
    unsorted_list = [1, 9, 3, 0, 6]
bubble_sort_example(unsorted_list)
