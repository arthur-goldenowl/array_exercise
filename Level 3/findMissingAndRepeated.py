arr = [7, 3, 4, 5, 5, 6, 2]

def findMissingAndRepeated(arr):
    n = len(arr)
    repeated = None

    total = n * (n + 1) // 2

    for i in range(n):
        if arr[abs(arr[i]) - 1] < 0:
            repeated = abs(arr[i])
        else:
            total -= abs(arr[i])
            arr[abs(arr[i]) - 1] *= -1

    missing = total

    return repeated, missing

repeated, missing = findMissingAndRepeated(arr)

print(repeated, missing)