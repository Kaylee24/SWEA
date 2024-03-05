import sys
sys.stdin = open('1959_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    maximum = 0
    s = 0
    if N == M:
        for i in range(N):
            s += Ai[i] * Bj[i]
        maximum = s
    elif N > M:
        for k in range(N - M + 1):
            s = 0
            for i in range(M):
                s += Ai[i + k] * Bj[i]
            if maximum < s:
                maximum = s
    else:
        for k in range(M - N + 1):
            s = 0
            for i in range(N):
                s += Ai[i] * Bj[i + k]
            if maximum < s:
                maximum = s

    print(f'#{t} {maximum}')