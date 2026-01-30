numbers = [int(input()) for _ in range(5)]

# Way 1
numbers.sort()

# # Way 2
# numbers = sorted([int(input()) for _ in range(5)])

average = sum(numbers) // len(numbers)
mid = numbers[2]

print(average)
print(mid)


# Solution 1 - statistics module
import statistics
numbers = [int(input()) for _ in range(5)]

print(int(statistics.mean(numbers)))
print(statistics.median(numbers))