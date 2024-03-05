import sys
sys.stdin = open('4834_input.txt')

# 테스트 케이스 수 입력받기
T = int(input())

# 각 테스트 케이스에 대해서 입력값 입력 받기
for t in range(1, T + 1):
    N = int(input())
    N_list = list(input())

    # # 딕셔너리 변수 설정하기
    # N_numbers = {}
    #
    # # 딕셔너리에 숫자를 key 값으로 하고, 각 숫자의 개수를 value 값으로 담기
    # for n in N_list:
    #     N_numbers.setdefault(n, N_list.count(n))
    #
    # # 최댓값이 여러 key 값일 때, 가장 큰 key 값을 선별하기
    # list_many = []
    # for n in N_list:
    #     if N_numbers[f'{n}'] == max(N_numbers.values()):
    #         list_many.append(n)
    # the_number = max(list_many)
    # maximum = max(N_numbers.values())
    #
    # # 출력하기
    # print(f'#{t} {the_number} {maximum}')


    # 조별 코드리뷰 → list.reverse()

    # 숫자 카드 별 개수를 담은 리스트 생성
    N_counts = [0] * 10
    for n in N_list:
        N_counts[int(n)] = N_list.count(n)

    # reverse 를 통해 카드 개수가 가장 큰 카드 중에서도 숫자가 큰 카드의 수를 출력
    N_counts.reverse()
    print(f'#{t} {9 - N_counts.index(max(N_counts))} {max(N_counts)}')


