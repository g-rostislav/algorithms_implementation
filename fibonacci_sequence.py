def fib(n: int) -> int:
    assert n >= 0, 'Param "n" must be positive integer num'

    if n <= 1:
        return n

    prev = 0
    curr = 1
    fib_i = None
    for i in range(2, n + 1):
        fib_i = prev + curr
        prev = curr
        curr = fib_i

    return fib_i


if __name__ == '__main__':
    n = int(input('N='))
    print(fib(n=n))