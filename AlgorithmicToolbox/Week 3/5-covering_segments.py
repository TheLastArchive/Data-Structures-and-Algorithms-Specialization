# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    points_range = []
    print(segments)
    for s in segments:
        temp_list = [point for point in range(s[0], s[-1]+1)]
        points_range.append(temp_list)
    #write your code here

    print(points_range)
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

if __name__ == '__main__':
    optimal_points([[3,9]])
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
