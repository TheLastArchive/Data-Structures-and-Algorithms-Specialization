# Uses python3
import sys

def optimal_weight(weight, bars):

    value = []
    #Construct 2D array
    for i in range(weight + 1):
        value.append([0] * (len(bars) + 1))
        
    for i in range(1, len(bars) + 1):
        for w in range(1, weight + 1):
            value[w][i] = value[w][i-1]
            if bars[i-1] <= w:
                val = value[w-bars[i-1]][i-1] + bars[i-1]
                if value[w][i] < val:
                    value[w][i] = val
    return value[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
