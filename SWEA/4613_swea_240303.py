import sys
sys.stdin = open('4613_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M  = map(int, input().split())
    data = [['A'] * M] + [list(input()) for _ in range(N)]   # 'W' : 흰색, 'B' : 파란색, 'R' : 빨간색

    minimum = N * M

    ws, bs, rs = 0, 0, 0
    for w in range(1, N - 1):
        ws += M - data[w].count('W')
        bs = 0
        for b in range(1, N - w):
            bs += M - data[w + b].count('B')
            rs = 0
            for r in range(1, N - w - b + 1):
                rs += M - data[w + b + r].count('R')
            result = ws + bs + rs
            if minimum > result:   # 이 경우에 대한 새로 칠해야 하는 칸의 개수가 이때까지의 최솟값보다 작다면 최솟값 업데이트
                minimum = result

    print(f'#{t} {minimum}')