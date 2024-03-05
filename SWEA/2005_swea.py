import sys
sys.stdin = open('2005_hw_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여
for t in range(1, T + 1):
    # 파스칼의 삼각형의 크기 N 입력
    N = int(input())

    # 파스칼의 삼각형 공통 시작 행 pascal = [1] 설정 및
    # 새로 계산해 줄 행에 해당하는 리스트 변수 pascal_renew 준비
    pascal = [1]
    pascal_renew = pascal[:]
    print(f'#{t}')   # 테스트 케이스 번호와
    print(*pascal)   # 첫 행 출력

    # 첫 행을 제외하고 파스칼의 삼각형 크기만큼 반복하며
    # 인덱스 기준으로 본인 앞의 인덱스와 해당 인덱스의 값 합한 값을 재할당
    for n in range(1, N):
        pascal_renew.append(0)   # IndexError 를 대비해서 미리 허수 추가
        for m in range(n):
            if m + 1 == n:   # 만약 제일 끝 index 수를 계산중이라면 앞의 인덱스 값만 할당
                pascal_renew[m + 1] = pascal[m]
            else:
                pascal_renew[m + 1] = pascal[m] + pascal[m + 1]
        print(*pascal_renew)   # 계산한 새 행 출력
        pascal = pascal_renew[:]   # 참조할 행에 계산한 새 행 재할당