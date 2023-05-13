# *을 n개 출력하되 w마다 줄바꿈하는 프로그램

n = int(input())
w = int(input())

for i in range(n):
    print('*', end="")
    if i % w == w - 1:
        print()
if n % w:
    print()
