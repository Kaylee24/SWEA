import sys
sys.stdin = open('5202_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]   # 화물차의 작업 시작 시간 s, 종료 시간 e

    data.sort(key=lambda x: x[1])

    # 첫번째 : data 첫번째 원소 (트럭)
    # 첫번째 트럭 도착시간보다 출발이 빠른 트럭들은 데이터에서 삭제
    # 두번째 : 남은 data 첫번째 원소 (트럭)
    # 데이터 리스트가 빌때까지 무한 반복 / 그러면서 카운팅

    cnt = 0
    while data:
        truck = data.pop(0)
        cnt += 1
        while data:
            if data[0][0] < truck[1]:
                data.pop(0)
            else:
                break

    print(f'#{t} {cnt}')