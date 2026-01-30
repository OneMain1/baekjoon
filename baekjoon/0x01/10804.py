def swap(a, b, numbers):
    n1 = a - 1
    n2 = b - 1
    
    new_list = list(range(1, 21))
    
    for i in range(20):
        if i < n1:
            new_list[i] = numbers[i]
        elif i >= n1 and i <= n2:
            new_list[i] = numbers[n2 + n1 - i]
        else:
            new_list[i] = numbers[i]
    
    return new_list

numbers = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    
    numbers = swap(a, b, numbers).copy()
    
print(*numbers)

# Solution 1 - Slicing
numbers = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    numbers[a-1:b] = numbers[a-1:b][::-1]
    
print(*numbers)