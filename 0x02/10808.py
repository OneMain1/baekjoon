counts = [0] * 26

for char in list(input()):
    counts[ord(char) - ord('a')] += 1
    
print(*counts)

# Solution 1 - Counter
from collections import Counter

c = Counter(input())
print(*[c.get(chr(i + ord('a')), 0) for i in range(26)])

# Solution 2
counts = [0] * 26

for char in input():
    counts[ord(char) - ord('a')] += 1
    
print(*counts)