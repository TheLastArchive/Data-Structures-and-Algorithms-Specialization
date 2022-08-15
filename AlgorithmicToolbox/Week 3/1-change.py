# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = 0
    while (m != 0):
        if (m - 10) >= 0:
            m -= 10
            coins += 1
        elif (m - 5) >= 0:
            m -= 5
            coins += 1
        else: return coins + m

    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = int(input())
    print(get_change(m))
