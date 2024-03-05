import sys
sys.stdin = open('1209_input.txt')

# 테스트 케이스 10개
# 각각의 테스트 케이스에 대해서
for t in range(1, 11):

    # 입력값 받기
    testcase = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 합을 담을 정수 변수, 합들을 담을 리스트 변수 설정
    sum_10 = 0
    sums = []

    # 행별로 합 구하기
    for i in range(100):
        for j in range(100):
            sum_10 += arr[i][j]
        sums.append(sum_10)
        sum_10 = 0

    # 열별로 합 구하기
    for j in range(100):
        for i in range(100):
            sum_10 += arr[i][j]
        sums.append(sum_10)
        sum_10 = 0

    # 좌측상단 - 우측하단 대각선 합 구하기
    for i in range(100):
        sum_10 += arr[i][i]
    sums.append(sum_10)
    sum_10 = 0

    # 좌측하단 - 우측상단 대각선 합 구하기
    for i in range(100):
        sum_10 += arr[i][100-i-1]
    sums.append(sum_10)
    sum_10 = 0

    # 합들 중에서 최댓값 구해서 출력하기
    result = max(sums)
    print(f'#{testcase} {result}')