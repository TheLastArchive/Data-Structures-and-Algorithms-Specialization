# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum     = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_fast(n):
    if n <= 1:
        return n
    
    _sum = calc_fib(n + 2) - 1

    return _sum % 10

    
def calc_fib(n):

    #Create an 'empty' list of size n
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_fast(n))
