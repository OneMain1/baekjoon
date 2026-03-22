"""
Problem 2: All Roads Lead to Rome

Task Description
You are given a map of the Roman Empire. There are N+1 cities (numbered from 0 to N)
and N directed roads between them. The road network is connected. All roads lead to
Rome, meaning there is a route from each city to Rome. Your task is to find Rome on
the map, or decide that it is not there.

Write a function `def solution(A, B)` that returns the number of the city which is
Rome. If no such city exists, return -1.

Rome is defined as a city that:
- Can be reached from every other city
- Has no outgoing roads (all roads lead TO Rome, not FROM Rome)

Examples:
- Given A = [0, 1, 2], B = [3, 3, 3], the function should return 3
  (city 3 can be reached from all cities 0, 1, 2)
- Given A = [0, 1], B = [1, 0], the function should return -1
  (circular dependency, no Rome exists)

Assumptions:
- N is an integer within the range [1..200,000]
- Each element of arrays A and B is an integer within the range [0..N]
- The road network is connected
- Arrays A and B have the same length equal to N
- Element (A[i], B[i]) represents a road from city A[i] to city B[i]
"""


def solution(A, B):
    pass
