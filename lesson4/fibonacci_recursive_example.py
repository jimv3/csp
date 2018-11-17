def fibonacci_recursive_example(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    
    return fibonacci_recursive_example(n - 1) + fibonacci_recursive_example(n - 2)

fibonacci_recursive_example(8)