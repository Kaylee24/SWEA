import sys
sys.stdin  = open('1234_extra_input.txt')

for t in range(1, 11):
    N, strings = input().split()
    N = int(N)
    strings = list(strings)

    # 스택을 활용하여 문자 하나하나 스택에 담고
    # 담기 전 담고자 하는 문자와 스택의 top 에 위치한 문자가 같으면
    # 문자를 담지 않고, 스택의 top 에 위치한 문자는 제거하여
    # 반복되지 않는 문자들만 담는다.
    stack = []
    top = -1
    for n in range(N):
        if top == -1:
            stack.append(strings[n])
            top += 1
        else:
            if strings[n] == stack[top]:
                stack.pop()
                top -= 1
            else:
                stack.append(strings[n])
                top += 1

    print(f'#{t}')
    print(''.join(stack))