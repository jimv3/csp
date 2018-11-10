known_search_types = {'binary_search': 'O(LOGN)', 'indexed_search': 'O(1)',
                    'sequential_search': 'O(N)', 'tree_search': 'O(LOGN)'}


def check_answer(search_type, answer):
    if search_type in known_search_types:
        return confirm_answer(search_type, answer)
    return f'Invalid sort type: {search_type}'


def confirm_answer(search_type, answer):
    if answer.replace(' ', '').upper() == known_search_types[search_type]:
        return 'Great job!'
    else:
        return 'Think about how many loops are executed and what controls the number of executions'
