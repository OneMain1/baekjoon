n = int(input())

while n > 0:
    for i in range(n):
        print("*", end='')

    print()
    n -= 1
    
# Solution 1 - range
n = int(input())

for i in range(n, 0, -1):
    print("*" * i)
    
# Solution 2 - join
n = int(input())

for i in range(n, 0, -1):
    print(''.join(['*'] * i))
    
# Solution 3 - reversed
n = int(input())

for i in reversed(range(1, n + 1)):
    print("*" * i)