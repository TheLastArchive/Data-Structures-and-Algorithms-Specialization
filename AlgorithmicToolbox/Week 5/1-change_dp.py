# Uses python3
import sys

def get_change(money):

    coins = [1,3,4]
    min_coins = [0] * (money + 1)
    #Check the possible combinations and pick the lowest one
    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                num_coins = min_coins[m - coin] + 1
                #Has this calculation been done before?
                if num_coins < min_coins[m] or min_coins[m] == 0:
                    min_coins[m] = num_coins

    return min_coins[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
