# timeout
chars = list(input())

n = int(input())

cursor = len(chars) - 1

for _ in range(n):
    com = input().split()
    if com[0] == 'P':
        chars.insert(cursor + 1, com[1])
        cursor += 1
    if com[0] == 'L' and cursor >= 0:
        cursor -= 1
    if com[0] == 'D' and cursor < len(chars):
        cursor += 1
    if com[0] == 'B' and cursor >= 0:
        del chars[cursor]
        cursor -= 1
        
print(''.join(chars))

# Solution 1
import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

n = int(input())

for _ in range(n):
    com = input().split()                                                                                                                       
    if com[0] == 'P':                                                                                                                           
        left.append(com[1])                                                                                                                     
    elif com[0] == 'L' and left:                                                                                                                
        right.append(left.pop())                                                                                                                
    elif com[0] == 'D' and right:                                                                                                               
        left.append(right.pop())                                                                                                                
    elif com[0] == 'B' and left:                                                                                                                
        left.pop()                                                                                                                              
                                                                                                                                                
print(''.join(left + right[::-1]))     