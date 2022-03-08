import sys
from math import gcd, lcm


# def lcm(a: int, b: int) -> int:
#     return a * b // gcd(a, b)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    print(gcd(N, M))
    print(lcm(N, M))
