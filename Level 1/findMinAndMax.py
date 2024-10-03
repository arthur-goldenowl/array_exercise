arr = [12, 1234, 45, 67, 1 ]

def findMinAndMax(arr):
    min = arr[0]
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    
    return min, max

min, max = findMinAndMax(arr)

print(min, max)