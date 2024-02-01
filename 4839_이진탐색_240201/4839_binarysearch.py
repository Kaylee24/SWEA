import sys
sys.stdin = open('4839_input.txt')


# 페이지를 이진 탐색으로 책을 펼쳐보는 횟수 구하는 함수
def findpage(P, A):
    start = 1
    end = P
    # page = int((start + end) / 2)
    count = 0
    while start <= end:
        page = int((start + end) / 2)
        count += 1
        if page > A:
            end = page
        elif page < A:
            start = page
        else:
            return count

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여 입력값 받기
for t in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    # A와 B의 이진 탐색 횟수를 비교하여 결과 출력
    if findpage(P, Pa) < findpage(P, Pb):
        print(f'#{t} A')
    elif findpage(P, Pa) > findpage(P, Pb):
        print(f'#{t} B')
    else:
        print(f'#{t} 0')