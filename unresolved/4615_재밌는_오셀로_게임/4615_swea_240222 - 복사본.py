import sys
sys.stdin = open('4615_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())   # N : 보드의 한 변의 길이(4, 6, 8), M : 플레이어가 돌을 놓는 횟수
    rocks = [list(map(int, input().split())) for _ in range(M)]   # 1 : 흑돌, 2 : 백돌 / [j + 1, i + 1, color]

    board = [[0]*N for _ in range(N)]
    board[N//2 - 1][N//2 - 1 : N//2 + 1] = [2, 1]
    board[N//2][N//2 - 1 : N//2 + 1] = [1, 2]

    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    for i in range(M):
        x = rocks[i][0] - 1
        y = rocks[i][1] - 1
        board[y][x] = rocks[i][2]          # 해당 칸 지정색으로 바꾸기
        for d in range(8):
            if (0 <= x + dx[d] < N) and (0 <= y + dy[d] < N):   # 범위 내에서
                if board[y + dy[d]][x + dx[d]] == rocks[i][2] or board[y + dy[d]][x + dx[d]] == 0:   # 조회한 칸의 돌이 같은 색이거나 빈칸이면
                    pass
                else:   # 조회한 칸의 돌이 다른 색 돌이면
                    board


        # 가로, 세로, 우측상단 대각선, 우측하단 대각선 순회하면서
        # 옆에 돌이 있는지 확인하고
        # 만약 돌이 현재칸과 다른 색이면
        # 같은 색이 나오는지 확인하고
        # 같은 색이 나오는 구간까지의 색을 바꾼다





    black = 0
    white = 0
    for i in range(N):
        black += board[i].count(1)
        white += board[i].count(2)
    print(f'#{t} {black} {white}')