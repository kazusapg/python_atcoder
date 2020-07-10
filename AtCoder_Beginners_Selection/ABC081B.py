n = map(int, input())
a_list = list(map(int, input().split()))

count = 0

f = False
while True:
    for i in a_list:
        if i % 2 == 1:
            f = True
            break

    if f:
        break

    count += 1
    a_list = [i / 2 for i in a_list]

print(count)
