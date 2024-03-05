'2차원 배열을 배우고, 풍선팡2 풀고 나서 다시 풀어봄'

import sys
sys.stdin = open('9490_input.txt')

# 테스트 케이스 수 입력받기
T = int(input())

# 각각의 테스트 케이스 별로 입력값 받기
for t in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우로 순회할 때 활용할 dx값 리스트 설정
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 꽃가루 합계 정보를 담을 리스트 설정
    flower_list = []
    
    # 모든 좌표를 순회하며 좌표 본인의 꽃가루 값에
    for i in range(N):
        for j in range(M):
            flowers = balloons[i][j]

            # flowers 는 계속해서 값을 더할 변수이므로
            # 변하지 않을 같은 값을 가진 변수를 하나 더 설정
            dx_flowers = flowers

            # 상하좌우로 순회할 때 활용할 dx값 리스트 설정
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]

            # 상하좌우 좌표의 꽃가루 값 더하기
            # 상하좌우로 해당 좌표의 꽃가루 값만큼의 좌표를 확인하기
            for k in range(4):
                for f in range(1, dx_flowers + 1):
                    ni = i + di[k] * f
                    nj = j + dj[k] * f

                    # 단, 주어진 범위를 벗어나지 않은 좌표에 대해서만 더한다.
                    if ni in range(N) and nj in range(M):
                        flowers += balloons[ni][nj]
            
            # 해당 좌표와 상하좌우의 좌표의 꽃가루를 전부 합하면
            # 위에서 미리 설정해놓은 리스트에 꽃가루 합계 정보 담기
            flower_list.append(flowers)

    # 결과 출력
    print(f'#{t} {max(flower_list)}')