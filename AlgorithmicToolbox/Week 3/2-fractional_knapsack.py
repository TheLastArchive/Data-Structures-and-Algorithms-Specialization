# Uses python3
import sys
import random

def get_optimal_value(capacity, weights, values):
    value = 0.

    val_per_weight = []
    for i in range(len(weights)):
        val_per_weight.append(values[i] / weights[i])

    while(capacity > 0 and len(weights) != 0):
        #Get the index of the most valuable item by weight
        i = val_per_weight.index(max(val_per_weight))
        #Can you take all of the most valuable?
        if weights[i] <= capacity:
            capacity -= weights[i]
            value += values[i]
        #If not, take as much as you can
        else:
            value += (capacity * val_per_weight[i])
            capacity = 0
        #Remove the item from lists
        weights.pop(i)
        values.pop(i)
        val_per_weight.pop(i)
    return value

def stress_test():
    while True:
        capacity = random.randint(0, 101)
        list_size = random.randint(0, 11)
        weights = []
        values = []

        for _ in range(0, list_size):
            weights.append(random.randint(1, 501))
            values.append(random.randint(1, 501))

        get_optimal_value(capacity, weights, values)


if __name__ == "__main__":
    # stress_test()
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
