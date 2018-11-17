def factorial_loops_correct(n):
    result = 1
    i = abs(n)
    while i > 1:
        result *= i
        i -= 1
    if n < 0:
        result *= -1
    return result


def factorial_recursive_correct(n):
    if abs(n) == 1:
        return n
    addition = 1
    if n < 0:
        addition = -1
    return n * factorial_recursive_correct(n-addition)


print(factorial_loops_correct(3))
print(factorial_loops_correct(-3))
print(factorial_recursive_correct(3))
print(factorial_recursive_correct(-3))
