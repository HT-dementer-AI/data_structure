from typing import Any, Sequence


# 아래와 같은 표현은 함수 어노테이션이라고 한다.
# 어노테이션은 함수의 매개변수와 반환값을 나타내는 역할을 한다.
# max_of(a: Sequence)
def max_of(a: Sequence):
    max = a[0]
    for i in range(1, len(a)):
        if(a[i] > max):
            max = a[i]

    return max


# C언어에서의 NULL값을 python에서 None라고 생각하면 된다.
if __name__ == '__main__':
    n = int(input())
    x = [None] * n

    for i in range(n):
        x[i] = int(input())

    print(max_of(x))
