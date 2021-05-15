#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    winner = 1
    while (n > 1):
        x = math.log(n,2)
        if int(x) == x:
            n = n // 2
        else:
            n = n - 2**math.floor(x)
        winner += 1
    if winner % 2 == 0:
        return 'Louise'
    else:
        return 'Richard'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()

