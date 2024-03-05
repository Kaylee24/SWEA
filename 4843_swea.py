import sys
sys.stdin = open('4843_im_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여 정수의 개수 N 과 N 개의 정수 입력
for t in range(1, T + 1):
    N = int(input())
    Ns = list(map(int, input().split()))

    # 특별히 정렬된 숫자를 담을 빈 리스트 준비
    special_Ns = []

    # 특별히 정렬된 숫자를 10개까지만 출력할 것이므로
    # 10번 특별히 정렬하는데
    # 짝수번째에는 최댓값을, 홀수번째에는 최솟값을 정렬한다.
    # (단, 이미 정렬한 값에 대해서는 더 이상 정렬하지 아니한다.)
    for n in range(10):
        if n % 2 == 0:
            special_Ns.append(max(Ns))
            Ns.pop(Ns.index(max(Ns)))
        else:
            special_Ns.append(min(Ns))
            Ns.pop(Ns.index(min(Ns)))

    # 조건에 맞춰 결괏값 출력
    print(f'#{t}', *special_Ns)