def quicksort(arr):
    left = []
    right = []
    pivot = arr[0]
    mid = []   
    for num in arr:
        if num >= pivot:
            right.append(num)
        elif num <= pivot:
            left.append(num)
        else:
            mid.append(num)
    return left+mid+right
        

n = int(input())
arr = list(map(int, input().split()))
ans = quicksort(arr)

for num in ans:
    print(num, end =' ')