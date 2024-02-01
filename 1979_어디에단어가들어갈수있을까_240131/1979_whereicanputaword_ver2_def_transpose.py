import sys
sys.stdin = open('1979_input.txt')

# row 를 기준으로 순회하며 연속된 흰칸의 길이 구하기
# 검정색 칸 또는 row 가 바뀔때 기준
def count_whites(N, K, puzzletable):
    count = 0
    for i in range(N):
        length = 0
        for j in range(N):
            if puzzletable[i][j] == 1:
                length += 1
            elif puzzletable[i][j] == 0:
                if length == K:
                    count += 1
                length = 0
        if length == K:
            count += 1
    return count

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):

    # 퍼즐판의 가로, 세로 길이(N)와 구하고자 하는 단어의 글자수(K),
    # 퍼즐판의 정보 입력
    N, K = map(int, input().split())
    puzzletable = [list(map(int, input().split())) for _ in range(N)]

    # 퍼즐판의 전치행렬 생성
    # count_whites() 함수가 row 기준으로만 조회하기 때문에 입력할 행렬을 함수에 맞게 준비
    trans_puzzletable = [[0] * N for _ in range(N)]
    for p in range(N):
        for q in range(N):
            trans_puzzletable[p][q] = puzzletable[q][p]

    # 결과 출력하기
    print(f'#{t} {count_whites(N, K, puzzletable) + count_whites(N, K, trans_puzzletable)}')