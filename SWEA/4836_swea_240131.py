import sys
sys.stdin = open('4836_input.txt')

# 테스트 케이스 입력받기
T = int(input())

# 각각의 테스트 케이스에 대해서
for t in range(1, T + 1):

    # 색을 숫자로 나타내고 있으므로
    # 흰색을 0으로 나타내어 10*10 격자 설정
    arr = [[0]*10 for _ in range(10)]

    # 색칠 영역의 수(N)와
    # 각각의 색칠 영역의 입력값 받고
    N = int(input())
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 색칠 영역을 격자에 반영
        # 주어진 정보에서 같은 색인 영역은 겹치지 않는다고 했으므로
        # 가능한 색상은 흰색 = 0, 빨강 = 1, 파랑 = 2, 보라 = 3
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color

    # 보라색 칸 수 변수 설정
    purple = 0

    # 전체 칸에 대하여 보라색 칸 수 세기
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                purple += 1

    # 최종 결과값 출력
    print(f'#{t} {purple}')