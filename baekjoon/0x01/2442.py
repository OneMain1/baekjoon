n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1), end='')
    print('' * (n - i), end='')
    
    print()
    
# Solution 1
n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
    
# Solution 2 - center()
n = int(input())

for i in range(1, n + 1):
    print(('*' * (2 * i - 1)).center(2 * n - 1).rstrip())
    
# Solution 3 - rjust()
n = int(input())

for i in range(1, n + 1):
    print(('*' * (2 * i - 1)).rjust(n + i - 1))