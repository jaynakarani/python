def getPairsCount(arr, n, sum):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1

    return count


number = list(map(int, input().split()))

sum = int(input())

print(getPairsCount(number,len(number),sum))