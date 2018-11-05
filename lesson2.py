known_sort_types = {'bubble_sort': 'O(N**2)', 'insertion_sort': 'O(N**2)',
                    'merge_sort': 'O(NLOGN)', 'quick_sort': 'O(N**2)', 'selection_sort': 'O(N**2)'}


def check_answer(sort_type, answer):
    if sort_type in known_sort_types:
        return confirm_answer(sort_type, answer)
    return f'Invalid sort type: {sort_type}'


def confirm_answer(sort_type, answer):
    if answer.replace(' ', '').upper() == known_sort_types[sort_type]:
        return 'Great job!'
    else:
        return 'Think about how many loops are executed and what controls the number of executions'
