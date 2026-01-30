list_num = []
list_odd = []
    
for _ in range(7):
    list_num.append(int(input()))
    
for i in range(len(list_num)):
    if list_num[i] % 2 == 1:
        list_odd.append(list_num[i])
        
if len(list_odd) == 0:
    print(-1)
else: 
    list_odd.sort()

    print(sum(list_odd))
    print(list_odd[0])
    
# Solution 1 - List Comprehension
numbers = [int(input()) for _ in range(7)]
odd_numbers = [num for num in numbers if num % 2 == 1]

if not odd_numbers:
    print(-1)
else:
    odd_numbers.sort()
    
    print(sum(odd_numbers))
    print(odd_numbers[0])

# Solution 2
odd_numbers = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        odd_numbers.append(num)
        
if not odd_numbers:
    print(-1)
else:
    odd_numbers.sort()
    
    print(sum(odd_numbers))
    print(odd_numbers[0])
    
# Solution 3 - min
odd_numbers = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        odd_numbers.append(num)
        
if not odd_numbers:
    print(-1)
else:
    print(sum(odd_numbers))
    print(min(odd_numbers))