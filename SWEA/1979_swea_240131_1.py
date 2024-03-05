import sys
sys.stdin = open('1979_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):

    # 퍼즐판의 가로, 세로 길이(N)와 구하고자 하는 단어의 글자수(K),
    # 퍼즐판의 정보 입력
    N, K = map(int, input().split())
    puzzletable = [list(map(int, input().split())) for _ in range(N)]

    # 흰칸의 길이 정보를 받을 리스트 설정
    whites = []

    # row 를 기준으로 순회하며 흰칸의 길이 구하기
    # row 가 바뀔때마다 구하던 흰칸의 값 리스트에 담기
    for i in range(N):
        length = 0
        for j in range(N):
            if puzzletable[i][j] == 1:
                length += 1
            elif puzzletable[i][j] == 0:
                whites.append(length)
                length = 0
        whites.append(length)

    # column 을 기준으로 순회하며 흰칸의 길이 구하기
    # column 이 바뀔때마다 구하던 흰칸의 값 리스트에 담기
    for j in range(N):
        length = 0
        for i in range(N):
            if puzzletable[i][j] == 1:
                length += 1
            elif puzzletable[i][j] == 0:
                whites.append(length)
                length = 0
        whites.append(length)

    # 주어진 조건(K)과 길이가 같은 흰칸의 개수를 담을 변수 설정
    count = 0
    
    # 주어진 조건(K)과 길이가 같은 흰칸의 개수 세기
    for white in whites:
        if white == K:
            count += 1

    # 결과 출력하기
    print(f'#{t} {count}')