import sys

words = ['dream', 'dreamer', 'erase', 'eraser']
s = input()

while s:
    for word in words:
        if s.endswith(word):
            s = s[:-len(word)]
            break
    else:
        print('NO')
        sys.exit()
print('YES')
