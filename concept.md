# Python Concepts - Baekjoon Problem Solving

## Input/Output Functions

### map()
Apply function to each element, returns iterator
- Memory efficient (lazy evaluation)
- Example: `map(int, input().split())`
- **IMPORTANT**: map object cannot be indexed directly
- Use unpacking: `a, b, c = map(int, input().split())` ✓
- DON'T append directly: `list.append(map(...))` ✗ (stores map object)
- Use `list(map(...))` for indexing or appending

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

### max() / min()
Find maximum/minimum value
- Works with multiple arguments: `max(a, b, c)`, `min(a, b, c)`
- Works with iterables: `max([1,2,3])`, `min([1,2,3])`
- Time complexity: O(n)
- Use `min()` to avoid sorting when only minimum needed

## Sorting

### sort() vs sorted()
Sorting functions
- `sort()`: in-place sorting, returns None (memory efficient)
- `sorted()`: returns new list
- Both use Timsort algorithm O(n log n)
- **Default: ascending order** (오름차순)
- For descending: add `reverse=True` parameter
- Example: `numbers.sort(reverse=True)` or `sorted(numbers, reverse=True)`
- **CRITICAL**: `[].sort()` returns None, not a list!

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

### len()
Get size/length of containers
- Works with lists, strings, sets, dictionaries
- Example: `len([1,2,3])` returns `3`
- Time complexity: O(1)

### List comprehensions
Create lists with filtering and transformation
- Syntax: `[expression for item in iterable if condition]`
- Example: `[x for x in numbers if x % 2 == 1]` (odd numbers)
- More readable than traditional loops
- Can replace filter() + map() combinations

### Division operators
Different types of division in Python
- `/` : Float division → `10 / 3 = 3.3333...`
- `//` : Integer division (floor) → `10 // 3 = 3`
- `%` : Modulo (remainder) → `10 % 3 = 1`
- Use `//` when result must be integer

### Modulo operator (%)
Calculate remainder after division
- `num % 2 == 1` checks if number is odd
- `num % 2 == 0` checks if number is even
- Common mistake: Don't confuse with bitwise AND (&)
- Example: `5 % 2 = 1`, `6 % 2 = 0`

### Empty list checking
Pythonic way to check if list is empty
- `if not list:` - preferred method
- `if len(list) == 0:` - also works but less pythonic
- Empty lists evaluate to False in boolean context

## Advanced Algorithms

### Dynamic Programming (DP)
Solve problems by breaking into subproblems and storing results
- **Key concepts**: Optimal substructure + Overlapping subproblems
- **3D DP**: `dp[i][j][k]` for multi-dimensional state tracking
- Example: `dp[i][j][k]` = using first i items, select j items, sum equals k
- Time complexity: O(n × select × target)

### Combinations (itertools)
Generate all possible combinations without repetition
- `combinations(iterable, r)` returns all r-length combinations
- Example: `combinations([1,2,3], 2)` → `(1,2), (1,3), (2,3)`
- Time complexity: O(C(n,r)) where C(n,r) = n!/(r!(n-r)!)
- Use for brute force when search space is small

### Function objects vs Function calls
Functions are first-class objects in Python
- `function_name` refers to function object (shows memory address)
- `function_name()` calls the function and returns result
- Functions can be assigned to variables and passed as arguments
- Example: `print(func)` vs `print(func())`

### Backtracking
Trace back through DP table to find actual solution path
- After DP confirms solution exists, reconstruct the path
- Check which transitions were taken in the DP table
- Build solution by reversing the decision sequence