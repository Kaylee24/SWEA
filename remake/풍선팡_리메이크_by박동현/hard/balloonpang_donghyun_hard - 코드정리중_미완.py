from copy import deepcopy
import sys
sys.stdin = open('input.txt')

def f(i, j, flower):
    balloon = flower[i][j]
    if flower[i][j] % 2 == 0:
        flower[i][j] = 0
        for dx in [1, -1]:
            balloon += flower[i + dx][j]
            flower[i + 1][j] = 0
            balloon += flower[i][j + dx]
            flower[i][j + dx] = 0
    elif flower[i][j] % 2 == 1:
        flower[i][j] = 0
        for dx in [1, -1]:
            balloon += flower[i + dx][j + dx]
            flower[i + 1][j + dx] = 0
            balloon += flower[i + dx][j - dx]
            flower[i + dx][j - dx] = 0
    return balloon



T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    flower.insert(0, [0] * (M + 2))
    flower.append([0] * (M + 2))

    max1 = 0
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            flower2 = deepcopy(flower)
            first = f(n, m, flower2)
            if ((flower[n][m] + first) % 2 == 0):
                for p in range(1, N + 1):
                    for q in range(1, M + 1):
                        flower3 = deepcopy(flower2)
                        second = f(p, q, flower3)
                        if max1 < first + second:
                            max1 = first + second
            else:
                if max1 < first:
                    max1 = first

    print(f'#{t} {max1}')