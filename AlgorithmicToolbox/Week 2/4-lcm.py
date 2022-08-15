# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a, b):
    #get the product for later
    product = a * b

    #First find the gcd
    while b != 0:
        newB = a % b
        a = b
        b = newB

    return int(product / a)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_fast(a, b))

