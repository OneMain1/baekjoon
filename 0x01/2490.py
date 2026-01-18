numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))
numbers3 = list(map(int, input().split()))

list1 = [numbers1, numbers2, numbers3]

for i in range(3):
    if sum(list1[i]) == 0:
        print("D")
    elif sum(list1[i]) == 1:
        print("C")
    elif sum(list1[i]) == 2:
        print("B")
    elif sum(list1[i]) == 3:
        print("A")
    elif sum(list1[i]) == 4:
        print("E")
        
# Solution - Dictionary
result_map = {0: "D", 1: "C", 2: "B", 3: "A", 4: "E"}

for _ in range(3):
    numbers = list(map(int, input().split()))
    print(result_map[sum(numbers)])
    

# Solution - List
results = ["D", "C", "B", "A", "E"]

for _ in range(3):
    numbers = list(map(int, input().split()))
    print(results[sum(numbers)])