# def fib(n: int) -> int:
#     if n == 0 or n == 1:
#         return 1

#     return fib(n-1) + fib(n-2)

# def fib(n: int) -> int:
#     if n == 0 or n == 1:
#         return 1

#     f1, f2 = 1, 1

#     for _ in range(n - 1):
#         f1, f2 = f2, f1 + f2

#     return f2


def fib_list(n: list) -> list[int]:
    result = [1] * n

    for i in range(2, len(result)):
        result[i] = result[i - 1] + result[i - 2]

    return result


def fib(n: int) -> int:
    return fib_list(n)[-1]

