n = int(input())

for i in range(1, 2 * n):
    if i <= n:
        print(' ' * (n - i) + '*' * (2 * i - 1))
    else:
        print(' ' * (i - n) + '*' * ((2 * (2 * n - i)) - 1))

# Solution 1 - abs()]
n = int(input())

for i in range(1 - n, n):
    stars = 2 * (n - abs(i)) - 1
    print(' ' * abs(i) + '*' * stars)
    
# Solution 2
n = int(input())                                                                                                                                
                                                                                                                                                
for i in range(1, n + 1):                                                                                                                       
    print(' ' * (n - i) + '*' * (2 * i - 1))                                                                                                    
                                                                                                                                                
for i in range(n - 1, 0, -1):                                                                                                                   
    print(' ' * (n - i) + '*' * (2 * i - 1))      