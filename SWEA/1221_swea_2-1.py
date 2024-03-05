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

    # 테스트 케이스의 인자를 정수형으로 변환하여 sort 메소드를 활용하기 위해
    # 변환에 활용할 숫자 정보 리스트 설정
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # 정수형으로 변환한 테스트 케이스를 담을 빈 리스트 설정
    integers = []

    # 테스트 케이스를 sort 메서드를 활용하기 위해 숫자로 인자 변환 및 저장
    for l in range(length):
        integers.append(numbers.index(strings[l]))

    # 정수형으로 인자 변환한 테스트 케이스 정렬
    integers.sort()

    # 인자를 다시 원래 값으로 대치해서 변환
    for l in range(length):
        strings[l] = numbers[integers[l]]

    # 결과 주어진 형식에 맞게 출력
    print(f'{testcase}')
    print(*strings)