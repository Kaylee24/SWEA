import sys
sys.stdin = open('5105_im_input.txt')

# 미로 길찾기 함수
def


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    print(maze)

    visited = []

    for n in range(N):
        if '2' in maze[n]:
            start = [n, maze[n].index('2')]
        if '3' in maze[n]:
            finish = [n, maze[n].index('3')]
        if start != [] and finish != []:
            break