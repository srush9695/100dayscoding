#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#

def minimumAverage(customers):
    customers.sort()  # sort by arrival time
    n = len(customers)

    heap = []
    time = 0
    i = 0
    total_wait = 0

    while i < n or heap:
        # add all arrived customers
        while i < n and customers[i][0] <= time:
            arrival, cook = customers[i]
            heapq.heappush(heap, (cook, arrival))
            i += 1

        if heap:
            cook, arrival = heapq.heappop(heap)
            time += cook
            total_wait += time - arrival
        else:
            # jump to next arrival time
            time = customers[i][0]

    return total_wait // n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
