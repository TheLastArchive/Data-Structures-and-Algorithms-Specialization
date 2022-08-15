# python3
import sys
import random
import time

def compute_min_refills(distance, tank, stops):

    stops_needed = 0
    dist_travelled = 0
    if stops[-1] == distance: stops.pop(-1)
    while stops:
        #How far the car can travel from the previous stop
        can_travel = tank + dist_travelled
        #Can you reach the end?
        if can_travel >= distance: return stops_needed
        #Add the furthest possible distance the car can travel and sort list
        stops.append(can_travel)
        stops.sort()
        #If tank + dist travelled is first in the list, it can't reach the next stop
        #Also check that the next element doesn't match incase it reaches the next stop exactly
        if stops[0] == can_travel != stops[1]: return -1

        i = stops.index(can_travel)
        #Remove the element we added
        stops.pop(i)
        #Edge case for only one stop or travel further than final stop
        if len(stops) == 1 or i >= len(stops):
            if stops[-1] + tank >= distance: return stops_needed + 1
            else: return -1
            
        #If it reaches a stop exactly, use that distance, else use the nearest stop
        # dist_travelled = stops[i] if stops[i] == (can_travel) else stops[i-1]
        if stops[i] == can_travel:
            dist_travelled = stops[i]
            del stops[:i+1]
        else:
            dist_travelled = stops[i-1]
            del stops[:i]
        stops_needed += 1

    if tank + dist_travelled >= distance: return stops_needed
    else: return -1

def stress_test():
    while True:
        random_list = []

        for _ in range(random.randint(0, 50000)):
            random_list.append(random.randint(0, 10000))

        print(compute_min_refills(random.randint(0, 10000),
        random.randint(1, 10000),
        random_list))
        time.sleep(5)

if __name__ == '__main__':
    # stress_test()
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
    # print(compute_min_refills(40, 40, [40, 81, 95]))

