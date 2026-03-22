"""
Problem 2: Balanced Split (Prefix Sum)

Task Description
You are given a string S consisting of N lowercase English letters.
Your task is to find the number of ways to split S into two non-empty
parts (Left and Right) such that at least one part contains the letter
'x' and the letter 'y' the same number of times.

Note that if a part contains neither 'x' nor 'y', the count for both
is 0, so they are considered "equal".

Goal: Write a function that returns the total number of valid split positions.

Example: S = "ayxbx"
- a / yxbx: Left (x:0, y:0) -> Valid
- ay / xbx: Left (x:0, y:1), Right (x:2, y:0) -> Invalid
- ayx / bx: Left (x:1, y:1) -> Valid
- ayxb / x: Left (x:1, y:1) -> Valid
Result: 3
"""


def solution(S):
    pass
