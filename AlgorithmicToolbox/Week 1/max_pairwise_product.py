import random


def max_pairwise_product(numbers):
    """Provided pairwise algorithm"""
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])


# def max_pairwise_product_fast(numbers):
#     #Pop the largest number then pop the next largest 
#     first = numbers.pop(numbers.index(max(numbers)))
#     second = numbers.pop(numbers.index(max(numbers)))

#     return first * second


def max_pairwise_product_fast(numbers):
    """Optimised pairwise product"""
    if len(numbers) < 2:
        return numbers

    #Sort list in ascending orders and multiply the 2 largest numbers
    numbers.sort()
    return numbers[-1] * numbers[-2]


def stress_test():
    while(True):
        array_size = random.randint(2, 10000)
        arr = []
        for i in range(array_size):
            arr.append(random.randint(0, 100000))

        slow = max_pairwise_product(arr)
        fast = max_pairwise_product_fast(arr)
        if fast != slow:
            print(f"Error: {fast} =/= {slow}")
        else: print("OK")


if __name__ == '__main__':
    # stress_test()
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(max_pairwise_product_fast(input_numbers))
