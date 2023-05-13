# for문을 사용할때 안에 조건문을 사용하는것이 아니라
# for문을 돌릴때 아래처럼 조건을 넣어주면 더 빨라짐

n = int(input())
w = int(input())

for _ in range(n // w):
    print('*' * w)

rest = n % w
if (rest):
    print("*" * rest)
