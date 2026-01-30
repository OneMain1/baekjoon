"""
Problem 1: Post Office Shelf (Stack/Set)

Task Description
A post office receives packages numbered 1 to N in sequential order.
N clients are waiting in a line to collect their specific packages.
Each client waits for one specific package, and clients must leave
the line in the order they are standing.

When a package arrives:
- If the client at the front of the line is waiting for this package,
  they collect it and leave.
- If not, the package is placed on a shelf.
- After a client leaves, the new person at the front of the line checks
  the shelf. If their required package is there, they collect it and
  leave immediately.

Goal: Write a function that returns the maximum number of packages
that will be stored on the shelf at any single time.

Constraints:
- N is an integer within the range [1..100,000].
- client is a permutation of integers from 1 to N.
"""


def solution(client):
    pass
