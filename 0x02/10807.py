n = int(input())

numbers = list(map(int, input().split()))
v = int(input())

count = 0

for num in numbers:
    if num == v:
        count += 1

print(count)

# Solution 1 - count()
n = int(input())
numbers = list(map(int, input().split()))
v = int(input())

print(numbers.count(v))

# Solution 2 - Counter
from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))
v = int(input())

print(Counter(numbers).get(v, 0))