from max import max_of

number = 0

x = []

while True:
    s = input("number의 값을 입력하세요")
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(max_of(x))
