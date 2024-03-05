import sys
sys.stdin = open('1258_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    kill = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    kill.insert(0, [0] * (n + 2))
    kill.append([0] * (n + 2))

    start = []
    dx = [[-1, 0], [0, -1]]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if kill[i][j] != 0 and kill[i + dx[0][0]][j + dx[0][1]] == 0 and kill[i + dx[1][0]][j + dx[1][1]] == 0:
                start.append([i, j])

    size = []
    dy = [[1, 0], [0, 1]]
    for s in start:
        keep_going = True
        for i in range(s[0], n + 1):
            for j in range(s[1], n + 1):
                if kill[i][j] == 0:
                    break
                elif kill[i][j] != 0 and kill[i + dy[0][0]][j + dy[0][1]] == 0 and kill[i + dy[1][0]][j + dy[1][1]] == 0:
                    size.append([i - s[0] + 1, j - s[1] + 1])
                    keep_going = False
                    break
            if keep_going == False:
                break

    size.sort(key=lambda x: (x[0] * x[1], x[0]))

    print(f'#{t} {len(size)}', end=' ')
    for s in size:
        print(s[0], s[1], end=' ')
    print()