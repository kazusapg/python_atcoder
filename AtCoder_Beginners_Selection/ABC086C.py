import sys

n = int(input())

current_t = 0
current_x = 0
current_y = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    needed_time = abs(t - current_t)
    x_diff = abs(x - current_x)
    y_diff = abs(y - current_y)
    if x_diff + y_diff > needed_time:
        print('No')
        sys.exit()

    if needed_time % 2 == 0:
        if (x_diff + y_diff) % 2 == 1:
            print('No')
            sys.exit()
    else:
        if (x_diff + y_diff) % 2 == 0:
            print('No')
            sys.exit()
    current_t = t
    current_x = x
    current_y = y
print('Yes')
