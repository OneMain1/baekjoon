# Python Concepts - Baekjoon Problem Solving

## Input/Output Functions

### map()
Apply function to each element, returns iterator
- Memory efficient (lazy evaluation)
- Example: `map(int, input().split())`

### list()
Convert iterable to list
- Stores all elements in memory
- Example: `list(map(int, input().split()))`

### Unpacking (*)
Pass container elements as individual arguments
- `print(*numbers)` outputs space-separated values
- Example: `print(*[1,2,3])` → `1 2 3`

## Data Processing

### sum()
Calculate sum of iterable elements
- Example: `sum([1,2,3])` returns `6`
- Often used with list comprehensions: `sum(x for x in range(10))`
- Time complexity: O(n)

### max()
Find maximum value
- Works with multiple arguments: `max(a, b, c)`
- Works with iterables: `max([1,2,3])`
- Time complexity: O(n)

## Sorting

### sort() vs sorted()
Sorting functions
- `sort()`: in-place sorting, returns None (memory efficient)
- `sorted()`: returns new list
- Both use Timsort algorithm O(n log n)

## Data Structures

### Dictionary
Key-Value pairs for fast lookups
- Syntax: `{key: value}` - key comes first, value comes second
- Example: `grades = {"Alice": 95, "Bob": 87}`
- Access: `grades["Alice"]` returns `95`
- Keys must be unique, values can be duplicated

### set()
Create collection of unique elements
- Remove duplicates: `set([1,2,2,3])` returns `{1,2,3}`
- Check uniqueness: `len(set(numbers))` vs `len(numbers)`
- Mathematical operations: union, intersection, difference

### Counter (collections)
Count occurrences of elements
- Returns dict-like object with counts
- Example: `Counter([1,2,2,3])` returns `Counter({2:2, 1:1, 3:1})`
- Methods: `most_common()`, `elements()`, `update()`

## Optimization Patterns

### Dictionary/List mapping
Replace long if-elif chains
- Dict: `result_map = {0: "D", 1: "C"}` → `result_map[value]`
- List: `results = ["D", "C"]` → `results[index]`
- O(1) lookup vs O(n) conditional chains

### Multiple input lines
Read several lines of data
- `for _ in range(n): input()` → read n lines
- Avoid storing unnecessary intermediate lists
- Process each line immediately when possible