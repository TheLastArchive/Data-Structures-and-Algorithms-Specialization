# Uses python3
import sys
# from tkinter import Y

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    period = 1
    while(True):
        previous, current = current, previous + current
        if (previous % m == 0 and current % m == 1): break
        period += 1

    fibNum = calc_fib(n % period)
    return fibNum % m 


def calc_fib(n):
    if (n <=1): return n

    #Create an 'empty' list of size n
    fib_nums = [None] * (n + 1)
    fib_nums[0] = 0
    fib_nums[1] = 1

    #Loop through the list from 2 onwards and add the previous 2 elements
    for i in range(2, n + 1):
        fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2]

    # print(fib_nums)
    return fib_nums[-1]
    

if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))

