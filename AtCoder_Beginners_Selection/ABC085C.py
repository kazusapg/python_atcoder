import sys

n, y = map(int, input().split())

for i in range(n + 1):
    for j in range(n - i + 1):
        k = n - i - j
        total = i * 10000 + j * 5000 + 1000 * k
        if total == y:
            print(i, j, k)
            sys.exit()
print(-1, -1, -1)
