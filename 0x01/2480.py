# Solution 1 - Counter
from collections import Counter
a, b, c = map(int, input().split())

count = Counter([a, b, c])

max_count = max(count.values())
if max_count == 3:
    ret = 10000 + a*1000
elif max_count == 2:
    for num, cnt in count.items():
        if cnt == 2:
            duplicated = num
        elif cnt == 1:
            unique = num
            
    # duplicated = [num for num, cnt in count.items() if cnt == 2][0]
    
    ret = 1000 + duplicated*100
else:
    ret = max(a, b, c)*100

print(ret)


# Solution 2 - Without Counter
a, b, c = map(int, input().split())

if a == b == c:
    ret = 10000 + a*1000
elif a == b or a == c:
    ret = 1000 + a*100
elif b == c:
    ret = 1000 + b*100
else:
    ret = max(a, b, c)*100
    
print(ret)

# Solution 3 - Set
a, b, c = map(int, input().split())

numbers = [a, b, c]
unique_set = set(numbers)

if len(unique_set) == 1:
    ret = 10000 + a * 1000
elif len(unique_set) == 2:
    duplicated = (sum(numbers) - sum(unique_set))
    ret = 1000 + duplicated * 100
else:
    ret = max(numbers) * 100
    
print(ret)