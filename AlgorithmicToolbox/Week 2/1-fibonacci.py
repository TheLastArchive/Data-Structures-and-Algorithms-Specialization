# Uses python3
# def calc_fib(n):
#"""The provided algorithm"""
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)

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


n = int(input())
print(calc_fib(n))
