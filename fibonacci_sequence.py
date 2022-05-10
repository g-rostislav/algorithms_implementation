def main(n: int) -> int:
    assert n >= 0, 'Param "n" must be positive integer num'
    if n == 0:
        return 0
    elif n == 1:
        return 1

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
    print(main(n=n))
    

