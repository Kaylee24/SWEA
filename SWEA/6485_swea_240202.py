import sys
sys.stdin = open('6485_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):
    
    # 버스 노선의 수와 정보, 정류장의 수와 정류장 번호 입력
    N = int(input())
    ABs = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    Cs = [int(input()) for _ in range(P)]

    # 각각의 버스 정류장의 지나가는 버스 노선 수 정보를 담을 리스트 준비
    C_lines = [0] * P

    # 버스 정류장마다 각각의 버스 노선이 지나가는지 확인하고 카운팅
    for p in range(P):
        for n in range(N):
            if ABs[n][0] <= Cs[p] <= ABs[n][1]:
                C_lines[p] += 1

    # 결과 출력
    print(f'#{t}', end=' ')
    print(*C_lines)