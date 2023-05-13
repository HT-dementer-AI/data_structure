# 세정수를 입력받아 중앙값 구하기
def med(a, b, c):
    if (a >= b):
        if (b >= c):
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


a = int(input())
b = int(input())
c = int(input())
print(f"중앙값은 {med(a,b,c)}입니다.")
