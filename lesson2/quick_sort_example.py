def quick_sort_example(items):
    high = len(items) - 1
    low = 0
    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(items, low, high)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
    return items


def partition(arr, low, high):
    i = (low - 1)
    x = arr[high]

    for j in range(low, high):
        if arr[j] <= x:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


unsorted_list = [1, 9, 3, 0, 6]
quick_sort_example(unsorted_list)
