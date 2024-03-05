'2차원 배열 배우기 전'

'''
풍선팡2 ⭢ 풍선팡 순으로 난이도가 어려운데
240130, 알고리즘 2일차에 풍선팡을 2차원 배열을 배우기 전에 먼저 풀고,
240131, 알고리즘 3일차에 2차원 배열 배우고, 풍선팡2 풀고, 다시 풍선팡을 풀어보았다.(ft_2)

풍선팡을 지민님이랑 같이 풀어서
다시 풀때도 같이 각자 풀어보았고,
그래서 지민님 두번째 버전 코드도 같이 첨부해 두었다.



처음 풀때는 가로, 세로로 2차원의 인덱스를 부여하고 싶었는데
정확한 방법을 몰라서 어려웠고,
range를 설정하는 것이 어려웠다.

2차원 배열을 배우고는
입력값을 받으면서 index 가 자동으로 부여할 수 있어서
훨씬 편했다.

그리고 dx를 통해서 상하좌우를 순회하는 것이 용이해졌다.

여기서 지민님과 코드가 달라지는데, 지민님은 di, dj를 다르게 설정하였다.
'''

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