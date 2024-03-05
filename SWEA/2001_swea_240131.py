import sys
sys.stdin = open('2001_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):

    # 입력값 입력
    N, M = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]

    # 파리채를 내려쳤을 때 죽는 파리의 수 합계를 담을 리스트 설정
    flies_list = []

    # 파리채의 넓이 범위를 지정할 때 사용할 dx 변수 리스트 설정
    dx = list(range(M))
    
    # 좌측상단을 기준점으로 하여 파리채가 범위를 벗어나지 않는 범위에 대하여
    # 죽일 수 있는 파리의 최대 수를 구하고자 하는 것이므로
    # 파리채가 범위의 일부만 잡는 경우는 제외하고 계산한다.
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            flies = 0
        
            # row 기준으로 순회
            for x in dx:
                di = i + x
            
                # column 기준으로 순회하여 죽는 파리의 수 더하기
                for x in dx:
                    dj = j + x
                    flies += N_list[di][dj]

            # 파리채를 한번 내리쳤을 때마다의 죽은 파리의 수를 리스트 변수에 담기
            flies_list.append(flies)

    # 죽은 파리의 수 중 최댓값 출력
    print(f'#{t} {max(flies_list)}')