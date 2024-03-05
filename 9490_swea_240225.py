import sys
sys.stdin = open('input/9490_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            k = flower[i][j]
            cnt = k
            for p in range(1, k + 1):
                for q in range(4):
                    if 0 <= i + di[q] * p < N and 0 <= j + dj[q] * p < M:
                        cnt += flower[i + di[q] * p][j + dj[q] * p]
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{t} {max_cnt}')