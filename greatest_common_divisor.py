def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


if __name__ == '__main__':
    a, b = list(int(el) for el in input().split())
    print(gcd(a, b))