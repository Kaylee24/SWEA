import sys
sys.stdin = open('1926_swea_input.txt')

N = int(input())

i = 1
while i < N + 1:
    num = list(str(i))
    cnt = 0
    for j in range(len(num)):
        if num[j] == '3' or num[j] == '6' or num[j] == '9':
            cnt += 1
    if cnt == 0:
        print(i, end=' ')
    else:
        print('-' * cnt, end=' ')
    i += 1