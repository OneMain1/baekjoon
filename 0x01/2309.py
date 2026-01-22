# Solution 1 - Brute Force
from itertools import combinations

numbers = [int(input()) for _ in range(9)]

for comb in combinations(numbers, 7):
    if sum(comb) == 100:
        result = sorted(comb)
        for num in result:
            print(num)
        break