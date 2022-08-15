# Uses python3
import re as regex
import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    min_mat, max_mat, n, ops = matrix(dataset)
    
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_mat[i][j], max_mat[i][j] = min_and_max(i, j, min_mat, max_mat, ops)

    return max_mat[0][-1]
  
        
def min_and_max(i, j, min_mat, max_mat, ops):
    min_val = sys.maxsize
    max_val = sys.maxsize * -1
    for k in range(i, j):

        a = evalt(max_mat[i][k], max_mat[k+1][j], ops[k])
        b = evalt(max_mat[i][k], min_mat[k+1][j], ops[k])
        c = evalt(min_mat[i][k], max_mat[k+1][j], ops[k])
        d = evalt(min_mat[i][k], min_mat[k+1][j], ops[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    
    return min_val, max_val


def matrix(dataset):
    #Split the values from the operators
    values = regex.split('\+|-|\*', dataset)
    ops = regex.split('\d', dataset)
    #Remove empty space
    ops = list(filter(None, ops))
    n = len(values)
    min_mat = []
    max_mat = []
    #Construct matrix
    for i in range(n):
        arr = [0] * (n)
        arr[i] = int(values[i])
        min_mat.append(arr)
        #Copy list or else you'll have the same list reference
        #I spent 3 hours debugging to try find that this was my issue...
        max_mat.append(arr.copy())
    return min_mat, max_mat, n, ops


if __name__ == "__main__":
    # print(get_maximum_value("5-8+7*4-8+9"))
    print(get_maximum_value(input()))
