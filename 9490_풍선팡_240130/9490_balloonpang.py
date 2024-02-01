import sys
sys.stdin = open('9490_input.txt')

# 테스트 케이스 수 입력받기
T = int(input())

# 각각의 테스트 케이스에 대하여 입력값 입력받기
for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 풍선 내의 꽃가루 정보를 담을 리스트 변수 설정
    balloon_list = []

    # 꽃가루 개수 마저 입력받기, 풍선의 좌우 가장자리에도 비어 있는 풍선들이 있다고 가정
    for n in range(N):
        balloons = list(map(int, input().split()))
        balloon_list.append(balloons)

    # 꽃가루가 들어있는 모든 좌표에 대하여 풍선이 터졌을때의 꽃가루 개수 계산하기
    def sum_flower(i, j):
        x = balloon_list[i][j]
        flower = 0
        for k in range(-x, x + 1):
            if i < -k or i > N - 1 - k:
                continue
            else:
                flower += balloon_list[i + k][j]
        for k in range(-x, x + 1):
            if j < -k or j > M - 1 - k:
                continue
            else:
                flower += balloon_list[i][j + k]
        flower -= x
        return flower
    flower_list = []

    for n in range(N):
        for m in range(M):
            flower_list.append(sum_flower(n, m))

    print(f'#{t} {max(flower_list)}')