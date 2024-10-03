arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
target = 0

def countPairsWithGivenSum(arr, target):
    count = 0
    numDict = {}

    for num in arr:
        complement = target - num
        if complement in numDict:
            count += numDict[complement]
        numDict[num] = numDict.get(num, 0) + 1

    return count


def findNonDupplicatePairsWithGivenSum(arr, target):
    pairs = []
    appeared = set()
    numDict = {}

    for num in arr:
        complement = target - num
        if complement in numDict:
            if (num, complement) not in appeared and (complement, num) not in appeared:
                pairs.append(sorted([num, complement]))
                appeared.add((num, complement))
                appeared.add((num, complement))
        numDict[num] = numDict.get(num, 0) + 1

    return sorted(pairs)

print(countPairsWithGivenSum(arr, target))
print(findNonDupplicatePairsWithGivenSum(arr, target))  