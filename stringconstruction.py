n = int(input())
for _ in range(n):
    str = input()
    visited = []
    cost = 0    
    for char in str:
        if char not in visited:
            cost +=1
            visited.append(char)
        else:
            cost +=0
    print(cost)          