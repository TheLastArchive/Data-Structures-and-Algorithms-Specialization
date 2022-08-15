# Uses python3
from collections import defaultdict
import sys

def get_majority_element(elements):

    #Probably not an ideal solution but it works pretty well
    #Create a default dictionary so no error when accessing a missing key
    count = defaultdict(int)
    for i in elements:
        count[i] += 1

    #Get the most prominent element with max
    values = count.values()
    max_value = max(values)   
    if max_value > (len(a) / 2): return True  

    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a):
        print(1)
    else:
        print(0)
