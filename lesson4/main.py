from IPython.core.magic import (
    register_line_magic, register_cell_magic, register_line_cell_magic)
from IPython.display import display


@register_line_magic
def hint(line):
    known_methods = {'fib': fibonacci_hint, 'qs': quick_sort_hint}
    method, which = line.split(' ')
    if method in known_methods:
        known_methods[method](int(which))
    else:
        display(f'Unknown hint request: {method}')


def fibonacci_hint(which):
    hints = {1: 'Think about the first two elements in the sequence',
             2: "Unless you pass 0 as the nth element you don't have to worry about it", 3: 'if n == 1 or n == 2:...'}
    if which not in hints:
        display(f'Requested hint ({which}) is out of range')
    else:
        display(hints[which])


def quick_sort_hint(which):
    hints = {1: 'Consider using a list comprehension to split the list', 2: 'Consider what the stopping condition is for quick sort', 3: 'if len(items) <= 1:...'}
    if which not in hints:
        display(f'Requested hint {which} is out of range')
    else:
        display(hints[which])
