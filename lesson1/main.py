def q1(answer):
    if answer == "O(n)":
        return "Great job!"
    elif answer == "O(n^2)":
        return "Think about how many times the for loop will be performed and try again."
    elif answer == "O(1)":
        return "O(1) is equivalent to constant time. This effectively means there is no difference regardless of the size of the input. Think about what is happening in the for loop and try again."

    return "Please choose from (a), (b), or (c)."

def q2(answer):
    if answer == "O(n^2)":
        return "Great job!"
    elif answer == "O(n)":
        return "Think about how many times the for loop will be performed and remember the rules for combining Big O."
    elif answer == "O(1)":
        return "O(1) is equivalent to constant time. This effectively means there is no difference regardless of the size of the input. Think about what is happening in the for loop and try again."

    return "Please choose from (a), (b), or (c)."

def q3(answer):
    if answer == "O(m + n)":
        return "Great job!"
    elif answer == "O(n^2)":
        return "Think about the how many times the for loops will be performed and remember the rules for combining Big O."
    elif answer == "O(1)":
        return "O(1) is equivalent to constant time. This effectively means there is no difference regardless of the size of the input. Think about what is happening in the for loop and try again."

    return "Please choose from (a), (b), or (c)."