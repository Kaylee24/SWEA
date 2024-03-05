import sys
sys.stdin = open('1244_swea_input.txt')

def sort_card(i):  # i 번째로 큰 수
    max_idx = board.index(max(board[i:]))
    print(max_idx)
    if max_idx != i:  # i 번째로 큰 수가 i 번째 자리의 수가 아니라면



T = int(input())
for t in range(1, T + 1):
    board, N = input().split()
    board = list(map(int, list(board)))
    N = int(N)

    board_sorted = board[:]
    board_sorted.sort(reverse=True)

    n = 0
    while 1:
        if board == board_sorted:
            break
        sort_card(n)
        n += 1


