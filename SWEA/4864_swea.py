import sys
sys.stdin = open('4864_im_input.txt')

# 첫번째 문자열이 두번째 문자열 내에 있는지 확인하는 함수
def find_string(str1, str2):
    if str1 in str2:
        return 1
    return 0

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여 문자열 2개 입력
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    
    # 결과 형식에 맞춰 함수 호출하여 출력
    print(f'#{t}', find_string(str1, str2))