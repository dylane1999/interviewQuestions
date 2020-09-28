from collections import Counter


def goodTuples(a):
    occurrences = {}
    count = 0
    windowArray = []
    for i in range(len(a) - 2):

        windowArray.append(a[i])
        windowArray.append(a[i + 1])
        windowArray.append(a[i + 2])

        occurrences = Counter(windowArray)
        for amount in occurrences:
            if occurrences[amount] > 2:
                count = count + 1
        windowArray = []
    return count
