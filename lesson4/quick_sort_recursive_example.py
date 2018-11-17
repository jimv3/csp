def quick_sort_recursive_example(items):
    if len(items) <= 1:
        return items
    first_value = items[0]
    return quick_sort_recursive_example([x for x in items if x < first_value]) + [first_value] + quick_sort_recursive_example([x for x in items if x > first_value])


unsorted_list = [1, 9, 3, 0, 6]
quick_sort_recursive_example(unsorted_list)
