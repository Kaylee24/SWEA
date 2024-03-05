import sys
sys.stdin = open('9367_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))

    max_cnt = 0
    cnt = 1
    for i in range(N - 1):
        if C[i + 1] > C[i]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt

    print(f'#{t} {max_cnt}')