#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    print(obstacles)
    d = set(map(tuple,obstacles))
    print(d)
    def go_right():
       i = r_q
       j = c_q
       res = 0
       while j < n:
        j += 1
        if (i,j) in d:
            break
        res += 1
       return res
    print(f'Right = {go_right()}')
    def go_left():
       i = r_q
       j = c_q
       res = 0
       while j > 1:
        j -= 1
        if (i,j) in d:
            break
        res += 1
       return res
    print(f'Left = {go_left()}')
    def go_up():
        res = 0
        i = r_q
        j = c_q
        while i < n :
            i += 1
            if (i,j) in d:
                break
            res += 1
        return res
    print(f'Up = {go_up()}')
    def go_down():
        res = 0
        i = r_q
        j = c_q
        while i > 1 :
            i -= 1
            if (i,j) in d:
                break
            res += 1
        return res
    print(f'Down = {go_down()}')
    def go_up_right():
        i = r_q
        j = c_q
        res = 0
        while i < n and j < n:
            i += 1
            j += 1
            if (i,j) in d:
                break
            res += 1
        return res
    print(f'Right Up = {go_up_right()}')
    def go_up_left():
        i = r_q
        j = c_q
        res = 0
        while i < n and j > 1:
            i += 1
            j -= 1
            if (i,j) in d:
                break
            res += 1
        return res
    print(f'Left Up = {go_up_left()}')
    def go_down_right():
        i = r_q
        j = c_q
        res = 0
        while i > 1 and j < n:
            i -= 1
            j += 1
            if (i,j) in d:
                break
            res += 1
        return res
    print(f'Down Right = {go_down_right()}')
    def go_down_left():
        i = r_q
        j = c_q
        res = 0
        while i > 1 and j > 1:
            i -= 1
            j -= 1
            if (i,j) in d:
                break
            res += 1
        return res
    print(f'Left  Down = {go_down_left()}')
    return go_right() + go_left() + go_up() + go_down() + go_up_right()+go_up_left() + go_down_right() + go_down_left()
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

