# lcm(a,b) = (a * b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


def lcm(a: int, b: int) -> int:
    return int(a * b / gcd(a, b))


if __name__ == '__main__':
    a, b = list(int(el) for el in input().split())
    print(lcm(a, b))

