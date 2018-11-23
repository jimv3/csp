from IPython.display import display


def q1(answer):
    if answer < 2:
        display('Think about what needs to be tracked. Are you allowing for the data as well as being able to iterate through the list?')
    elif answer == 2:
        display('Great job! Yes, there will need to be a pointer to the data and a pointer to the next element in the list.')
    else:
        display('Think about what needs to be tracked. What elements MUST a node be aware of? Remember, this is the minimal number of pointers for a forward-only linked list.')


def q2(answer):
    if answer < 3:
        display('Think about what needs to be tracked. Are you allowing for the data as well as being able to iterate through the list in both directions?')
    elif answer == 3:
        display('Great job! Yes, there will need to be a pointer to the data, a pointer to the next element in the list, and a pointer to the previous element in the list.')
    else:
        display('Think about what needs to be tracked. What elements MUST a node be aware of? Remember, this is the minimal number of pointers for a doubly-linked list.')


def check_answer(question, answer):
    questions = {'q1': q1, 'q2': q2}
    if question in questions:
        questions[question](answer)
    else:
        display(f'The question submitted, {question}, is not recognized.')
