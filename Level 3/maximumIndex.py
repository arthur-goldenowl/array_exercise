arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]

def max(a,b):
    return a if a > b else b

def min(a,b):
    return a if a < b else b

def maxIndexDiff(arr):
    leftMin = [0] * len(arr)
    rightMax = [0] * len(arr)

    leftMin[0] = arr[0]
    for i in range(1, len(arr)):
        leftMin[i] = min(arr[i], leftMin[i-1])

    rightMax[len(arr)-1] = arr[len(arr)-1]
    for i in range(len(arr) - 2, -1, -1):
        rightMax[i] = max(arr[i], rightMax[i+1])
    
    i, j = 0, 0
    indexI, indexJ = 0, 0
    maxDiff = -1
    while (j < len(arr) and i < len(arr)):
        if (leftMin[i] <= rightMax[j]):
            if (j - i > maxDiff):
                maxDiff = j - i
                indexI = i
                indexJ = j
            j += 1
        else:
            i += 1

    return indexI, indexJ, maxDiff

i, j, diff = maxIndexDiff(arr)
print(i, j, diff)

