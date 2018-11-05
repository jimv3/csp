from IPython.core.magic import (
    register_line_magic, register_cell_magic, register_line_cell_magic)
from IPython.display import display


@register_line_magic
def show(line):
    "my line magic"
    answer = eval(line + '()')
    display(answer)


def bubble_sort():
    return 'def bubble_sort(items):\n   return boo'
