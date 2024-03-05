import sys
sys.stdin = open('input.txt')

from copy import deepcopy

def f(i, j, flower):
    global balloon
    balloon += flower[i][j]
    if flower[i][j] % 2 == 0:
        flower[i][j] = 0
        balloon += flower[i - 1][j]
        flower[i - 1][j] = 0
        balloon += flower[i + 1][j]
        flower[i + 1][j] = 0
        balloon += flower[i][j - 1]
        flower[i][j - 1] = 0
        balloon += flower[i][j + 1]
        flower[i][j + 1] = 0
    elif flower[i][j] % 2 == 1:
        flower[i][j] = 0
        balloon += flower[i - 1][j - 1]
        flower[i - 1][j - 1] = 0
        balloon += flower[i + 1][j + 1]
        flower[i + 1][j + 1] = 0
        balloon += flower[i - 1][j + 1]
        flower[i - 1][j + 1] = 0
        balloon += flower[i + 1][j - 1]
        flower[i + 1][j - 1] = 0
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
            balloon = 0
            flower2 = deepcopy(flower)
            first = f(n, m, flower2)
            if ((flower[n][m] + balloon) % 2 == 0):
                for p in range(1, N + 1):
                    for q in range(1, M + 1):
                        balloon = 0
                        flower3 = deepcopy(flower2)
                        f(p, q, flower3)
                        if max1 < first + balloon:
                            max1 = first + balloon
            else:
                if max1 < first:
                    max1 = first

    print(f'#{t} {max1}')