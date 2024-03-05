import sys
sys.stdin = open('1244_swea_input.txt')

def sort_card(i):  # i 번째로 큰 수
    if i == N:
        global max_v
        max_v = max(max_v, int(''.join(board)))
        return

    for p in range(L-1):
        for q in range(p+1, L):
            board[p], board[q] = board[q], board[p]
            result = ''.join(board)
            if (i, result) not in visir:
                sort_card(i+1)
                visit.append((i, result))
            board[p], board[q] = board[q], board[p]


T = int(input())
for t in range(1, T + 1):
    board, N = input().split()
    board = list(map(int, list(board)))
    N = int(N)

    L, max_v = len(board), 0
    visit = []
    sort_card(0)

    print(f'#{t} {max_v}')