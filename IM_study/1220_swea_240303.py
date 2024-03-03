import sys
sys.stdin = open('1220_swea_input.txt')

for t in range(1, 11):
    L = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]   # 1 : N, 2 : S

    cnt = 0
    for j in range(100):       # 세로 기준으로 먼저 순회(크게 순회)
        column = []
        for i in range(100):   # 해당 세로줄에서 하나씩 순회
            if table[i][j] == 1:
                column.append(table[i][j])
            elif table[i][j] == 2 and column != []:
                cnt += 1
                column = []

    print(f'#{t} {cnt}')