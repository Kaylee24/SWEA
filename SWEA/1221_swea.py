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

    # 테스트 케이스를 sort 메서드를 활용하기 위해 숫자로 인자 변환
    for l in range(length):
        if strings[l] == 'ZRO':
            strings[l] = 0
        elif strings[l] == 'ONE':
            strings[l] = 1
        elif strings[l] == 'TWO':
            strings[l] = 2
        elif strings[l] == 'THR':
            strings[l] = 3
        elif strings[l] == 'FOR':
            strings[l] = 4
        elif strings[l] == 'FIV':
            strings[l] = 5
        elif strings[l] == 'SIX':
            strings[l] = 6
        elif strings[l] == 'SVN':
            strings[l] = 7
        elif strings[l] == 'EGT':
            strings[l] = 8
        elif strings[l] == 'NIN':
            strings[l] = 9

    # 정수형으로 인자 변환한 테스트 케이스 정렬
    strings.sort()

    # 인자를 다시 원래 값으로 대치해서 변환
    for l in range(length):
        if strings[l] == 0:
            strings[l] = 'ZRO'
        elif strings[l] == 1:
            strings[l] = 'ONE'
        elif strings[l] == 2:
            strings[l] = 'TWO'
        elif strings[l] == 3:
            strings[l] = 'THR'
        elif strings[l] == 4:
            strings[l] = 'FOR'
        elif strings[l] == 5:
            strings[l] = 'FIV'
        elif strings[l] == 6:
            strings[l] = 'SIX'
        elif strings[l] == 7:
            strings[l] = 'SVN'
        elif strings[l] == 8:
            strings[l] = 'EGT'
        elif strings[l] == 9:
            strings[l] = 'NIN'

    # 결과 주어진 형식에 맞게 출력
    print(f'{testcase}')
    print(*strings)