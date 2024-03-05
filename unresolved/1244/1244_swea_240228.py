import sys
sys.stdin = open('1244_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    board, N = input().split()   # 숫자판의 정보 board, 교환 횟수 N

    board = list(map(int, board))

    N = int(N)
    print(N)
    while N > 0:
        N -= 1
        m = board.index(max(board))
        if m != 0:   # 가장 큰 수가 제일 앞에 있지 않다면
            max_num = board.pop(m)
            print(max_num, end='')
        else:
            print(board[0], end='')

    if N < len(board):
        # print("".join(board[N:]))
        print(*board[N:], sep="")
    else:
        print()