n = int(input())

time = list(map(int, input().split()))

M = 0
Y = 0

for i in range(n):
    term = time[i] // 30
    Y += (1 + term) * 10
    
for i in range(n):
    term = time[i] // 60
    M += (1 + term) * 15
    
if Y == M:
    print("Y M", Y)
elif M > Y:
    print("Y", Y)
else:
    print("M", M)