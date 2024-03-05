import sys
sys.stdin = open('4873_im_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여 문자열 입력
for t in range(1, T + 1):
    string = list(input())   # 문자열의 일부를 지우는 등 변경을 해야 하므로 list 자료형으로 변환

    # 반복문자가 없을 때까지 문자열의 반복 문자 지우기
    finish = False   # 반복문자를 지우는 순회 종료 조건 변수
    while finish == False:
        # 문자열의 모든 문자에 대하여 반복 문자 여부 확인 후 삭제
        # 반복 문자를 삭제하면 재할당된 문자열에 대해 다시 순회
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                string.pop(i + 1)
                string.pop(i)
                break
        # 반복문자가 없으면 순회 종료
        else:
            finish = True

    # 결과 출력
    print(f'#{t} {len(string)}')