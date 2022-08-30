# python3

from collections import deque


def given_solution(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums


def max_sliding_window(sequence, window_size):

    window = deque(sequence[:window_size])
    queue = deque(sequence[window_size:])
    maximums = []
    curr_max = 0
    while True:
        #This will only happen once
        if curr_max == 0:
            curr_max = max(window)

        maximums.append(curr_max)
        #If the queue is empty, all checks have been completed
        if len(queue) == 0: 
            return maximums

        new_val = queue.popleft()
        window.append(new_val)
        
        if new_val > curr_max: 
            curr_max = new_val
        if window.popleft() == curr_max:
            curr_max = max(window)


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

