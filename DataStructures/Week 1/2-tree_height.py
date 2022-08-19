# python3
import sys
import threading
from collections import deque, defaultdict


def compute_height(n, parents):
    
    #Create a dict for all the parents and their indices
    #{node1: [i1, i2,.... in]}
    values = defaultdict(list)
    for i in range(len(parents)):
        values[parents[i]].append(i)
    
    #Add the index of the root node to the queue
    depth = 0
    queue = deque(values[-1])
    while True:
        depth += 1
        new_queue = deque()
        while len(queue) != 0:
            node = queue.popleft()
            #Add children of all queued nodes to next queue
            for child in values[node]:
                new_queue.append(child)
        #If there are no children left, you've reached the bottom of tree  
        if len(new_queue) == 0: return depth
        queue = new_queue


def main():
    # print(compute_height(5, [4,-1,4,1,1]))
    # print(compute_height(10, [9,7,5,5,2,9,9,9,2,-1]))
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
