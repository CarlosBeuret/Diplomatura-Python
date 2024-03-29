from functools import cache


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


print(factorial(4))