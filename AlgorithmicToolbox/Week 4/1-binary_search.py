#This implementation works, however failed grading for being too slow
#I rewrote this in Java which runs much quicker

def binary_search_recursive(keys, query, lower, upper):
    pivot = int((upper - lower) / 2) + lower

    if pivot -1 == upper or pivot + 1 == lower: 
        return -1
    elif keys[pivot] == query: 
        return keys.index(query)
    elif keys[pivot] > query: 
        return binary_search_recursive(keys, query, lower, pivot - 1)
    else: 
        return binary_search_recursive(keys, query, pivot + 1, upper)


def binary_search_iterative(keys, query):
    lower = 0
    upper = len(keys) - 1
    while True:
        pivot = int((upper - lower) / 2) + lower
        if pivot -1 == upper or pivot + 1 == lower: 
            return -1
        elif keys[pivot] == query: 
            return keys.index(query)
        elif keys[pivot] > query: 
            upper = pivot - 1
        else: 
            lower = pivot + 1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_iterative(input_keys, q), end=' ')
        # print(binary_search_recursive(input_keys, q, 0, len(input_keys) - 1), end=' ')
