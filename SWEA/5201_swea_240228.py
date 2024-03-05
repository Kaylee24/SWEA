import sys
sys.stdin = open('5201_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())      # 컨테이너 수 N, 트럭 수 M
    W = list(map(int, input().split()))   # N개의 화물 무게
    T = list(map(int, input().split()))   # M개 트럭의 적재용량

    W.sort(reverse=True)
    T.sort(reverse=True)

    # 무게랑 적재용량 비교해서
    # 만약에 적재가 가능하다면 총 무게에 더하고 둘다 pop(0)
    # 만약에 적재가 불가능하다면 (무게 > 적재용량)
    # 무게를 제한다.

    total = 0
    while W and T:
        if W[0] <= T[0]:
            total += W[0]
            T.pop(0)
        W.pop(0)

    print(f'#{t} {total}')