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

### Input patterns
Choose correct pattern based on input format
- Single number: `n = int(input())`
- Multiple numbers on one line: `nums = list(map(int, input().split()))`
- Multiple lines, one number each: `nums = [int(input()) for _ in range(n)]`
- **Common mistake**: `int(input().split())` ✗ → int() can't convert list
- **Common mistake**: `map(int, input())` for single number ✗ → returns map object

### split()
Split string into list by delimiter
- `input().split()` - splits by whitespace
- Example: `"P x".split()` → `['P', 'x']`
- Example: `"L".split()` → `['L']` (single element)
- Warning: accessing `[1]` when only 1 element causes IndexError

### input() vs sys.stdin.readline()
Fast input for competitive programming
- `input()` - automatically removes newline
- `sys.stdin.readline()` - includes newline (`\n`)
- Example: input "abc" → `input()` = `"abc"`, `readline()` = `"abc\n"`
- `sys.stdin.readline()` is much faster for large input
- Use `.rstrip()` to remove newline: `sys.stdin.readline().rstrip()`

### list()
Convert iterable to list
- Stores all elements in memory
- Example: `list(map(int, input().split()))`

### Unpacking (*)
Pass container elements as individual arguments
- `print(*numbers)` outputs space-separated values
- Example: `print(*[1,2,3])` → `1 2 3`

### print() end parameter
Control line ending in print output
- Default: `end='\n'` (newline)
- Use `end=' '` for space-separated output on same line
- Use `end=''` for no separator
- Example: `for i in range(3): print(i, end=' ')` → `0 1 2 `
- Useful when printing multiple values in a loop on one line

## String Methods

### Single vs Double Quotes
Single quotes and double quotes are identical in Python
- `'P' == "P"` → `True`
- Both create the same string
- Useful for quotes inside quotes: `"It's okay"`, `'He said "Hi"'`

### center() / rjust() / ljust()
String alignment methods for padding
- `s.center(width)` - center align, add spaces on both sides
- `s.rjust(width)` - right align, add spaces on left
- `s.ljust(width)` - left align, add spaces on right
- Example: `'*'.center(5)` → `'  *  '`
- Example: `'*'.rjust(5)` → `'    *'`
- **Warning**: `center()` adds spaces on both sides, may cause BOJ format error

### rstrip() / lstrip() / strip()
Remove whitespace from strings
- `s.rstrip()` - remove trailing (right) whitespace
- `s.lstrip()` - remove leading (left) whitespace
- `s.strip()` - remove both sides
- **BOJ tip**: use `rstrip()` to fix format errors from trailing spaces
- Example: `'  *  '.rstrip()` → `'  *'`

### join()
Join iterable elements into a single string
- `'separator'.join(list)` - join list with separator
- Example: `'\n'.join(['a', 'b', 'c'])` → `'a\nb\nc'`
- Example: `' '.join(['hello', 'world'])` → `'hello world'`
- Useful for multi-line output: `print('\n'.join(lines))`

### ord() / chr()
Convert between characters and ASCII codes
- `ord(char)` - character → ASCII code
- `chr(code)` - ASCII code → character
- Example: `ord('a')` → `97`, `chr(97)` → `'a'`
- Alphabet index: `ord(char) - ord('a')` → 'a'=0, 'b'=1, ...
- Alphabet count: `counts[ord(char) - ord('a')] += 1`

### String is iterable
Strings can be iterated directly without list()
- `for char in "abc":` ✓ (can iterate directly)
- `for char in list("abc"):` ✗ (unnecessary conversion)
- Use `for char in input():` instead of `list(input())`

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

### abs()
Return absolute value of a number
- Useful for symmetric patterns: use `abs(i)` with `range(1-n, n)`
- Example: `abs(-3)` → `3`, `abs(3)` → `3`
- Diamond pattern: `' ' * abs(i) + '*' * (2 * (n - abs(i)) - 1)`

### count()
Count occurrences of a value in a sequence
- `list.count(value)` - count value in list
- `str.count(substr)` - count substring in string
- Example: `[1,2,2,3].count(2)` → `2`
- Example: `'abab'.count('a')` → `2`
- Simpler than Counter for basic counting

## Sorting

### sort() vs sorted()
Sorting functions
- `sort()`: in-place sorting, returns None (memory efficient)
- `sorted()`: returns new list
- Both use Timsort algorithm O(n log n)
- **Default: ascending order**
- For descending: add `reverse=True` parameter
- Example: `numbers.sort(reverse=True)` or `sorted(numbers, reverse=True)`
- **CRITICAL**: `[].sort()` returns None, not a list!

## Data Structures

### List - Adding Elements
Methods to add elements to a list
- `append(x)` - add to end, O(1)
- `insert(i, x)` - insert at index i, O(n)
- Example: `lst.append('d')` → add 'd' to end
- Example: `lst.insert(2, 'x')` → insert 'x' at index 2
- `append()` is more efficient for adding to end

### List - Removing Elements
Methods to remove elements from a list
- `del lst[i]` - delete at index i, no return value
- `lst.pop(i)` - delete at index i and return the value
- `lst.pop()` - delete and return last element, O(1)
- Example: `del lst[2]` → delete index 2
- Example: `x = lst.pop(2)` → delete index 2 and store value
- Middle deletion is O(n), end deletion is O(1)

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
- `c.get(key, default)` - return default if key not found (prevents KeyError)
- Example: `Counter('aab').get('c', 0)` → `0`

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

### reversed()
Reverse iteration over a sequence without modifying original
- Returns reverse iterator (not a list)
- Memory efficient - doesn't create a copy
- Example: `reversed(range(1, n + 1))` → iterate n, n-1, ..., 2, 1
- Works with sequences: lists, tuples, strings, range objects
- Compare: `range(n, 0, -1)` vs `reversed(range(1, n + 1))` (same result)
- Use `list(reversed(...))` to create reversed list

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

### Slice assignment
Replace a section of a list in-place using slice assignment
- `list[a:b] = new_values` replaces elements from index a to b-1
- Reverse a sublist: `list[a:b] = list[a:b][::-1]`
- `[::-1]` creates a reversed copy of the slice
- Example: `numbers[2:5] = numbers[2:5][::-1]` reverses indices 2,3,4
- Useful for partial list manipulation without rebuilding the entire list

### Advanced slicing
Slice with start, stop, and step for flexible list manipulation
- `list[-2::-1]` - reverse from second-to-last (exclude last)
- `list[::2]` - even indices only
- `list[1::2]` - odd indices only
- Example: `[1,2,3,4,5][-2::-1]` → `[4,3,2,1]`
- Diamond pattern: `top + top[-2::-1]` (top + reverse excluding peak)

### Built-in name shadowing
Never use built-in function names as variable/parameter names
- `list`, `map`, `int`, `str`, `sum`, `max`, `min` etc. are built-in functions
- Using them as names shadows the built-in: `list = [1,2,3]` → `list()` no longer works
- Causes `TypeError: 'list' object is not callable`
- **Fix**: Use descriptive names like `nums`, `result`, `items` instead
- Example: `def func(list):` ✗ → `def func(nums):` ✓

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

### Two Stack Technique
Use two stacks for efficient cursor-based editing (BOJ 1406)
- `left` stack: characters to the left of cursor
- `right` stack: characters to the right (stored in reverse)
- All operations O(1):
  - P x: `left.append(x)` - add left of cursor
  - L: `right.append(left.pop())` - move cursor left
  - D: `left.append(right.pop())` - move cursor right
  - B: `left.pop()` - delete left of cursor
- Output: `''.join(left + right[::-1])`
- **Key insight**: `insert()`/`del` in middle is O(n), stack end operations are O(1)