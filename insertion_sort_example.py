def insertion_sort_example(items):
    j = 0
    k = 0
    item_to_insert = None
    still_looking = False

    for k in range(1, len(items)):
        item_to_insert = items[k]
        j = k-1
        still_looking = True
        while j >= 0 and still_looking:
            if item_to_insert < items[j]:
                items[j+1] = items[j]
                j -= 1
            else:
                still_looking = False
        items[j+1] = item_to_insert
    return items


unsorted_list = [1, 9, 3, 0, 6]
insertion_sort_example(unsorted_list)
