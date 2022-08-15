# Uses python3
import sys

def optimal_sequence(number):
    sequence = []
    ops = [2,3]
    min_ops = [0] * number
    
    for n in range(2, number + 1):
        num_ops = min_ops[n - 2] + 1
        if num_ops < min_ops[n-1] or min_ops[n-1] == 0:
            min_ops[n-1] = num_ops
        for op in ops:
            if n % op == 0:
                num_ops = min_ops[(n-1) // op] + 1
                if num_ops < min_ops[n-1] or min_ops[n-1] == 0:
                    min_ops[n-1] = num_ops

    num_ops = min_ops[-1]
    while num_ops >= 0:
        sequence.append(len(min_ops) - min_ops[::-1].index(num_ops))
        num_ops -= 1

    return reversed(sequence)
  


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
