t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    possiblesums = [0] * (k+1)
    for i in range(1,k+1):
        for num in arr:
            if num <= i:
                possiblesums[i] = max(possiblesums[i],possiblesums[i-num]+num)
    print(possiblesums[k])