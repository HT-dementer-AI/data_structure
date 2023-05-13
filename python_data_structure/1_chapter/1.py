# 세 정수를 입력받아 최댓값 구하기

print("세정수의 최댓값을 구한다")

a = int(input())
b = int(input())
c = int(input())

max = a
if b > max:
    max = b
if c > max:
    max = c

print(f"최댓값은 {max}입니다.")
