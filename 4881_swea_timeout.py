import sys
sys.stdin = open('4881_im_input.txt')


def f(i, N, lst):
    global sums
    if i == N:
        s = 0
        for k in range(N):
            s += nums[k][lst[k]]
            # if s >= min(sums):
            #     break
        sums.append(s)
    else:
        for j in range(i, N):
            lst[i], lst[j] = lst[j], lst[i]
            f(i + 1, N, lst)
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for n in range(N):
        lst.append(n)

    sums = []

    f(0, N, lst)
    print(f'#{t}', min(sums))