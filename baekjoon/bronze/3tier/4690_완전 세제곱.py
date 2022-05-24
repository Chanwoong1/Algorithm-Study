# https://www.acmicpc.net/problem/4690

for i in range(5, 101) :
    tmp = i ** 3
    for a in range(2, i - 2) :
        for b in range(a, i - 1) :
            for c in range(b, i) :
                if a ** 3 + b ** 3 + c ** 3 == tmp :
                    print('Cube = {}, Triple = ({},{},{})'.format(i, a, b, c))