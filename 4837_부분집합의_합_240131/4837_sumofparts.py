import sys
sys.stdin = open('4837_input.txt')

# 집합 A
A = list(range(1, 13))

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):

    # 부분집합 원소의 수(N)와 부분 집합의 합(K) 입력
    N, K = map(int, input().split())

    # 부분집합의 집합과 부분집합 변수 설정
    # parts = []
    # part = []

    # 부분집합 만들기
    def make_parts(whole):
        parts = []
        for i in range(1 << len(whole)):
            part = []
            for j in range(len(whole)):
                if i & (1 << j):
                    part.append(whole[j])
            parts.append(part)
        return parts

    # 부분집합 중 원소의 수가 조건(N)과 같은 부분집합만 선별하기
    same_N = []
    for part in make_parts(A):
        if len(part) == N:
            same_N.append(part)

    # 원소의 수가 조건(N)과 같은 부분집합 중 원소들의 합이 조건(K)와 같은 부분집합만 선별하기
    same_K = []
    for same in same_N:
        if sum(same) == K:
            same_K.append(part)

    # 최종선별한 두 조건을 만족하는 부분집합의 수 출력하기
    result = len(same_K)
    print(f'#{t} {result}')