import sys
sys.stdin = open('4615_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())   # N : 보드의 한 변의 길이(4, 6, 8), M : 플레이어가 돌을 놓는 횟수
    rocks = [list(map(int, input().split())) for _ in range(M)]   # 1 : 흑돌, 2 : 백돌 / [j + 1, i + 1, color]

    board = [[0]*N for _ in range(N)]
    board[N//2 - 1][N//2 - 1 : N//2 + 1] = [2, 1]
    board[N//2][N//2 - 1 : N//2 + 1] = [1, 2]

    dx = [1, -1]

    for i in range(M):
        x = rocks[i][0] - 1
        y = rocks[i][1] - 1
        board[y][x] = rocks[i][2]
        for d in dx:
            for n in range(1, N):
                if (0 <= x + d < N) and (board[y][x + d] != 0):
                    if 0 <= x + d * n < N:
                        if rocks[i][2] == 1 and board[y][x + d * n] == 2:
                            board[y][x + d * n] = 1
                        elif rocks[i][2] == 2 and board[y][x + d * n] == 1:
                            board[y][x + d * n] = 2

                if (0 <= y + d < N) and (board[y + d][x] != 0):
                    if 0 <= y + d * n < N:
                        if rocks[i][2] == 1 and board[y + d * n][x] == 2:
                            board[y + d * n][x] = 1
                        elif rocks[i][2] == 2 and board[y + d * n][x] == 1:
                            board[y + d * n][x] = 2

                if (0 <= x + d < N) and (0 <= y + d < N) and (board[y + d][x + d] != 0):
                    if (0 <= x + d * n < N) and (0 <= y + d * n < N):
                        if rocks[i][2] == 1 and board[y + d * n][x + d * n] == 2:
                            board[y + d * n][x + d * n] = 1
                        elif rocks[i][2] == 2 and board[y + d * n][x + d * n] == 1:
                            board[y + d * n][x + d * n] = 2

                if (0 <= x + d < N) and (0 <= y - d < N) and board[y - d][x + d] != 0:
                    if (0 <= x + d * n < N) and (0 <= y - d * n < N):
                        if rocks[i][2] == 1 and board[y - d * n][x + d * n] == 2:
                            board[y - d * n][x + d * n] = 1
                        elif rocks[i][2] == 2 and board[y - d * n][x + d * n] == 1:
                            board[y - d * n][x + d * n] = 2

    black = 0
    white = 0
    for i in range(N):
        black += board[i].count(1)
        white += board[i].count(2)
    print(f'#{t} {black} {white}')