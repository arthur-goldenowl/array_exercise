arr = [1, 2, 3, 5]
n = 5

def findMissingNumber(arr, n):
    total = n * (n + 1) // 2
    for i in range(len(arr)):
        total -= arr[i]
    return total

print(findMissingNumber(arr, n))