# 1부터 n까지의 정수 합 구하기 while

n = int(input())

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1


print(f"총합 : {sum}")
