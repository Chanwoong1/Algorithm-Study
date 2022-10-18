# https://www.acmicpc.net/problem/4375

from contextlib import nullcontext
from doctest import BLANKLINE_MARKER


while (1) :
    try :
        n = int(input())
    except :
        break
    
    num = 0
    i = 1
    while (1) :
        num = num * 10 + 1
        num %= n
        if num == 0 :
            print(i)
            break
        i += 1