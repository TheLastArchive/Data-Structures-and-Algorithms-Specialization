# Uses python3
from multiprocessing.sharedctypes import Value
import sys
import itertools

def partition3(nums):
    #Quick check
    if sum(nums) % 3 != 0 or sum(nums) == 0: return 0
    target_value = nums // 3
    #Sort list in descending order
    nums.sort(reversed=True)
    # for c in itertools.product(range(3), repeat=len(A)):
    #     sums = [None] * 3
    #     for i in range(3):
    #         sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

    #     if sums[0] == sums[1] and sums[1] == sums[2]:
    #         return 1

    return 0


# val = "17 59 34 57 17 23 67 1 18 2 59"
# val2 = val.split(" ")
# val3 = [eval(i) for i in val2]
# val3.sort(reverse=True)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

