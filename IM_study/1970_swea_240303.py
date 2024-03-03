import sys
sys.stdin = open('1970_swea_input.txt')

def f(i):
    global N

    while N >= money[i]:
        N -= money[i]
        cnt[i] += 1

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    cnt = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(8):
        f(i)

    print(f'#{t}')
    print(*cnt)