import sys
sys.stdin = open('2001_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for p in range(M):
                for q in range(M):
                    cnt += flies[i + p][j + q]
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{t} {max_cnt}')