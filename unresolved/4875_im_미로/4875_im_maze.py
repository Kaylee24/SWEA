import sys
sys.stdin = open('4875_im_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def findway(x, y):
        for k in range(4):
            x += dx[k]
            y += dy[k]
            if



    for i in range(N):
        for j in range(N):
            for k in range(4):
                y = i + dy
                x = j + dx
                if maze[y][x] == 3:
                    print(f'#{T} 1')
    else:
        print(f'#{T} 0')


    result = 0
    print(f'#{T} {result}')