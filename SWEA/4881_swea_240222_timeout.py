import sys
sys.stdin = open('4881_swea_input.txt')

def f(i, cnt):
    global cnts
    global indexs
    if i == N:
        cnts.append(cnt)
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                f(i+1, cnt + number[i][j])
                visited[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    cnts = []
    f(0, 0)

    print(f'#{t} {min(cnts)}')