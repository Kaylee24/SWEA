import sys
sys.stdin = open('1961_extra_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):
    # 행렬의 정보 입력
    N = int(input())
    Ns = [list(input().split()) for _ in range(N)]
    
    # 결괏값을 담을 배열 준비
    result = [[''] * 3 for _ in range(N)]
    
    # 행렬을 순회하며
    # 첫번째 column 에는 90도 회전한 모양을,
    # 두번째 column 에는 180도 회전한 모양을,
    # 세번째 column 에는 270도 회전한 모양을 담는다.
    for n in range(N):
        for m in range(N):
            result[n][0] += Ns[N - 1 - m][n]
            result[n][1] += Ns[N - 1 - n][N - 1 - m]
            result[n][2] += Ns[m][N - 1 - n]

    # 조건에 맞게 결과 출력
    print(f'#{t}')
    for res in result:
        print(*res)