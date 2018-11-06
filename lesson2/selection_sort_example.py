def selection_sort_example(items):
    min_index = 0
    for j in range(len(items)-1):
        min_index = items.index(min(items[j:]))
        if min_index != j:
            items[j], items[min_index] = items[min_index], items[j]
    return items


unsorted_list = [1, 9, 3, 0, 6]
selection_sort_example(unsorted_list)
