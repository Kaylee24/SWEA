import sys
sys.stdin = open('4861_im_input.txt')

def palindrome(N, M, Ns):
    # 회문을 찾았을 때 현재 테스트 케이스에 대한 조회는 중지하기 위한 조건 변수 설정
    stop = False

    # 행별로 순회
    for i in range(N):
        # 길이가 M 이 되도록 행 내에서 순회하며 슬라이싱
        for j in range(N - M + 1):
            Ms = Ns[i][j: j + M]
            # 회문인지 확인하기 위해 슬라이싱한 리스트 복제
            reversed_Ms = Ms[::-1]
            # 회문인지 확인
            if Ms == reversed_Ms:
                print(f'#{t}', end=' ')
                print(''.join(Ms))
                stop = True
                break
        if stop == True:
            break

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):
    # 입력값 입력
    N, M = map(int, input().split())
    Ns = [list(input()) for _ in range(N)]

    # 전치행렬 준비
    reversed_Ns = [[0] * N for _ in range(N)]
    for p in range(N):
        for q in range(N):
            reversed_Ns[p][q] = Ns[q][p]

    # 함수 호출
    palindrome(N, M, Ns)
    palindrome(N, M, reversed_Ns)