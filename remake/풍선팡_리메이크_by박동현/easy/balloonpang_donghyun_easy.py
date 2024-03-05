import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]

    max_balloon = 0
    for n in range(1, N - 1):
        for m in range(1, M - 1):
            balloon = flower[n][m]
            if flower[n][m] % 2 == 0:
                balloon += flower[n - 1][m]
                balloon += flower[n + 1][m]
                balloon += flower[n][m - 1]
                balloon += flower[n][m + 1]
            elif flower[n][m] % 2 == 1:
                balloon += flower[n - 1][m - 1]
                balloon += flower[n + 1][m + 1]
                balloon += flower[n - 1][m + 1]
                balloon += flower[n + 1][m - 1]
            if max_balloon < balloon:
                max_balloon = balloon

    print(f'#{t} {max_balloon}')