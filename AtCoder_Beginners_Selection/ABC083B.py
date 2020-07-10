nab = list(map(int, input().split()))
n = nab[0]
a = nab[1]
b = nab[2]

s = 0

for i in range(1, n + 1):
    sum_num = sum([int(c) for c in str(i)])
    if a <= sum_num <= b:
        s += i
print(s)
