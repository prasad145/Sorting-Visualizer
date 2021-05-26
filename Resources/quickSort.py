import random
def partition(arr, l, r):
    # partition function is to bring all the elemets less the pivot to the left and greater than pivot to the right
    i = l - 1
    pivot = arr[r]

    for j in range(l, r):
        if(arr[j] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i] #swap index i and j 

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def partitionRandom(arr, l, r):
    if(l < r):
        randomIndex = random.randrange(l, r)
        arr[r], arr[randomIndex] = arr[randomIndex], arr[r]
    return partition(arr, l, r)

def quickSort(arr, l, r):
    res = "DONE"
    if r == 0:
        return arr
    if(l < r):
        pi = partitionRandom(arr, l, r) #partion index
        quickSort(arr, l, pi - 1)
        quickSort(arr, pi + 1, r)  
    return res

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print(quickSort(arr, 0, n - 1))
print(arr)