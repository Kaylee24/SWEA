import sys
sys.stdin = open('1221_hw_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(T):
    # 테스트 케이스 번호와 테스트 케이스의 길이 문자열로 입력
    testcase, length = map(str, input().split())
    # 테스트 케이스의 길이는 정수형으로 변환 후 재할당
    length = int(length)
    # 테스트 케이스 입력
    strings = list(input().split())

    # 테스트 케이스 정렬에 활용할 숫자 정보 리스트 설정
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # 정렬한 테스트 케이스를 담을 빈 리스트 설정
    result = []

    # 정렬하고자 하는 순서대로 같은 값의 인자의 수만큼 빈 리스트에 담기
    for number in numbers:
        for i in range(strings.count(number)):
            result.append(number)

    # 결과 주어진 형식에 맞게 출력
    print(f'{testcase}')
    print(*result)