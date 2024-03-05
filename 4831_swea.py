import sys
sys.stdin = open('4831_im_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):
    # 한번 충전으로 이동할 수 있는 최대 정류장 수 K,
    # 종점 정류장 번호 N, 충전기가 설치된 정류장 수 M,
    # M 개의 정류장 번호 입력
    K, N, M = map(int, input().split())
    busstops = [0] + list(map(int, input().split()))

    # 첫번째 정류장을 제외한 모든 정류장을 순회하며
    # 이전 정류장과의 거리가 K 보다 큰지 확인
    # 한번 충전으로 이동할 수 있는 최대 정류장 수 K 보다 간격이 먼 버스 정류장이 있다면 결괏값 0 할당
    for m in range(M):
        if busstops[m] - busstops[m-1] > K:
            print(f'#{t} 0')
            break

    else:
        # 현재 위치 current, 충전 횟수 count, 확인할 정류장들만 담을 빈 리스트 waitlist 변수 설정
        current = 0
        count = 0
        waitlist = 0
        finish = False

        # 현재 위치 current 가 종점 N 에 도달하기 전까지
        while current + K < N:
            if waitlist + K >= N:
                print(f'#{t} {count + 1}')
                finish = True
                break
            # 이전에 지나간 버스정류소들은 목록에서 제한다.
            busstops.pop(0)
            # 현재 위치로부터 한번 충전으로 갈 수 있는 거리 내의 버스정류소들을 waitlist 에 담는다.
            if current < busstops[0] <= current + K:
                waitlist = busstops[0]
            # 만일 버스정류소가 K 의 범위를 벗어나면
            # 현재 위치를 가장 마지막 버스정류소로 재할당하고
            # 충전 횟수도 1회 더해준다.
            else:
                current = waitlist
                count += 1
                busstops.insert(0, 0)