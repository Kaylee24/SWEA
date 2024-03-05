def f(i, cnt):
    global min_sum

    if i == N:              # 모두 더했으면
        if min_sum > cnt:   # 최종 합의 값을 합들의 최솟값과 비교해서 업데이트
            min_sum = cnt
    elif cnt > min_sum:     # 백트래킹 - 합의 값이 최솟값을 넘어서면 함수 실행 중단
        return

    else:
        for j in range(N):  # 열을 순회하면서
            if visited[j] == 0:
                visited[j] = 1
                f(i + 1, cnt + number[i][j])
                visited[j] = 0

import sys
sys.stdin = open('4881_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_sum = 10 * N
    f(0, 0)

    print(f'#{t} {min_sum}')