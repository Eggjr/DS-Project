# list to be sorted
import random
import copy
import matplotlib.pyplot as plt
import numpy as np

pauseTime = 0.001

bubbleAmount = 20
bubbleList = np.random.randint(1, 101, bubbleAmount)
bubblex = np.arange(0, bubbleAmount, 1)
bubbleColors = ["blue" for _ in range(bubbleAmount)]

selectionAmount = 20
selectionList = np.random.randint(1, 101, selectionAmount)
selectionx = np.arange(0, selectionAmount, 1)
selectionColors = ["blue" for _ in range(selectionAmount)]

insertionAmount = 20
insertionList = np.random.randint(1, 101, insertionAmount)
insertionx = np.arange(0, insertionAmount, 1)
insertionColors = ["blue" for _ in range(insertionAmount)]

mergeAmount = 50
mergeList = [random.randint(0, 101) for _ in range(mergeAmount)]
mergex = np.arange(0, mergeAmount, 1)
mergeColors = ['blue' for _ in range(mergeAmount)]

heapAmount = 50
heapList = np.random.randint(1, 101, heapAmount)
heapx = np.arange(0, heapAmount, 1)
heapColors = ["blue" for _ in range(heapAmount)]

quickAmount = 50
quickList = np.random.randint(1, 101, quickAmount)
quickx = np.arange(0, quickAmount, 1)
quickColors = ["blue" for _ in range(quickAmount)]

shellAmount = 20
shellList = np.random.randint(1, 101, shellAmount)
shellx = np.arange(0, shellAmount, 1)
shellColors = ["blue" for _ in range(shellAmount)]

bucketAmount = 50
bucketList = np.random.randint(1, 101, bucketAmount)
bucketx = np.arange(0, bucketAmount, 1)
bucketColors = ["blue" for _ in range(bucketAmount)]

# list2 = [random.randint(1, 51) for _ in range(0, 101)]

#
# def makeScrambledList(l1):
#     copylist = copy.copy(l1)
#     retL = []
#     for i in range(len(copylist)):
#         rand = random.randint(0, len(copylist) - 1)
#         retL.append(copylist.pop(rand))
#     return retL


def bubbleSort(l):
    n = len(l)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            bubbleColors[j+1], bubbleColors[j] = "red", "red"
            plt.bar(bubblex, l, color = bubbleColors)
            plt.title("Bubble Sort O(n$^{2}$)")
            plt.pause(pauseTime)
            plt.clf()
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
            bubbleColors[j], bubbleColors[j+1] = 'blue', 'blue'
        if not swapped:
            break


def selectionSort(l):
    n = len(l)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            selectionColors[i], selectionColors[j], selectionColors[minIndex] = 'red', 'red', 'green'
            plt.bar(selectionx, l, color = selectionColors)
            plt.title("Selection Sort O(n$^{2}$)")
            plt.pause(pauseTime)
            plt.clf()
            if l[minIndex] > l[j]:
                selectionColors[minIndex] = 'blue'
                minIndex = j
            selectionColors[j],selectionColors[minIndex] = 'blue', 'blue'
        selectionColors[i] = 'blue'
        l[i], l[minIndex] = l[minIndex], l[i]


def insertionSort(l):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i - 1
        insertionColors[i] = 'red'
        plt.bar(insertionx, l, color=insertionColors)
        plt.title("Insertion Sort O(n$^{2}$)")
        plt.pause(pauseTime)
        plt.clf()
        lcopy = copy.copy(l)
        while j >= 0 and key < l[j]:
            insertionColors[j] = 'red'
            plt.bar(insertionx, lcopy, color=insertionColors)
            plt.title("Insertion Sort O(n$^{2}$)")
            plt.pause(pauseTime)
            plt.clf()
            insertionColors[j] = 'blue'
            l[j + 1] = l[j]
            j -= 1
        insertionColors[i]= 'blue'
        l[j + 1] = key


def mergeSort(lst, left, right):
    if left >= right:
        return
    mid = (left+right)//2
    plt.bar(list(range(mergeAmount)), lst, color = mergeColors)
    plt.title("Merge Sort O(nlog$_{2}$n)")
    plt.pause(pauseTime)
    plt.clf()
    mergeSort(lst, left, mid)
    mergeSort(lst, mid+1,right)
    merge(lst, left, right, mid)
    plt.bar(list(range(mergeAmount)), lst, color = mergeColors)
    plt.title("Merge Sort O(nlog$_{2}$n)")
    plt.pause(pauseTime)
    plt.clf()


def merge(lst, left, right, mid):
    leftCopy = lst[left:mid+1]
    rightCopy = lst[mid+1:right+1]
    leftCounter, rightCounter = 0, 0
    sortedCounter = left
    while leftCounter < len(leftCopy) and rightCounter < len(rightCopy):
        if leftCopy[leftCounter] <= rightCopy[rightCounter]:
            lst[sortedCounter] = leftCopy[leftCounter]
            leftCounter += 1
        else:
            lst[sortedCounter] = leftCopy[leftCounter]
            rightCounter += 1
        sortedCounter +=1
    while leftCounter < len(leftCopy):
        lst[sortedCounter] = leftCopy[leftCounter]
        leftCounter += 1
        sortedCounter += 1
    while rightCounter < len(rightCopy):
        lst[sortedCounter] = rightCopy[rightCounter]
        rightCounter += 1
        sortedCounter += 1


# end of Sorting Algorithms Covered in CSA

def heapSort(l):
    def heapify(l, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        plt.bar(heapx, l, color=heapColors)
        plt.title("Heap Sort O(nlog$_{2}$n)")
        plt.pause(pauseTime)
        plt.clf()
        if left < n and l[largest] < l[left]:
            largest = left
        if right < n and l[largest] < l[right]:
            largest = right
        if largest != i:
            l[i], l[largest] = l[largest], l[i]
            heapify(l, n, largest)

    n = len(l)
    for i in range(n // 2 - 1, -1, -1):
        heapify(l, n, i)
    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0)


def quickSort(l):
    def partition(l, low, high):
        pivot = l[high]
        quickColors[high] = 'green'
        i = low - 1
        for j in range(low, high):
            quickColors[j] = 'red'
            plt.bar(quickx, l, color=quickColors)
            plt.title("Quick Sort O(nlog$_{2}$n)")
            plt.pause(pauseTime)
            plt.clf()
            if l[j] <= pivot:
                quickColors[i] = 'blue'
                i = i + 1
                quickColors[i] = 'red'
                l[i], l[j] = l[j], l[i]
                quickColors[j] = 'blue'
                quickColors[i], quickColors[j] = quickColors[j], quickColors[i]
            quickColors[j] = 'blue'
        l[i + 1], l[high] = l[high], l[i + 1]
        return i + 1

    n = len(l)

    def recQuickSort(l, low, high):
        plt.bar(quickx, l, color=quickColors)
        plt.title("Quick Sort O(nlog$_{2}$n)")
        plt.pause(pauseTime)
        plt.clf()
        if low < high:
            pi = partition(l, low, high)
            recQuickSort(l, low, pi - 1)
            recQuickSort(l, pi + 1, high)

    recQuickSort(l, 0, n - 1)


def shellSort(l):
    n = len(l)
    gap = n // 2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                shellColors[i+gap], shellColors[i] = 'yellow', 'yellow'
                plt.bar(shellx, l, color=shellColors)
                plt.title("Shell Sort O(n$^{2}$)")
                plt.pause(pauseTime)
                plt.clf()
                if l[i + gap] >= l[i]:
                    shellColors[i + gap], shellColors[i] = 'blue', 'blue'
                    break
                else:
                    shellColors[i + gap], shellColors[i] = 'red', 'red'
                    plt.bar(shellx, l, color=shellColors)
                    plt.title("Shell Sort O(n$^{2}$)")
                    plt.pause(5*pauseTime)
                    plt.clf()
                    l[i + gap], l[i] = l[i], l[i + gap]
                    plt.bar(shellx, l, color=shellColors)
                    plt.title("Shell Sort O(n$^{2}$)")
                    plt.pause(5*pauseTime)
                    plt.clf()
                shellColors[i + gap], shellColors[i] = 'blue', 'blue'
                i = i - gap
            j += 1
        gap = gap // 2


def bucketSort(l):
    def insertion(l):
        n = len(l)
        for i in range(1, n):
            key = l[i]
            j = i - 1
            plt.bar([i for i in range(len(l))], l)
            plt.title("Bucket Sort O(nlog$_{2}$n)")
            plt.pause(pauseTime)
            plt.clf()
            lcopy = copy.copy(l)
            while j >= 0 and key < l[j]:
                plt.bar([i for i in range(len(l))], lcopy)
                plt.title("Bucket Sort O(nlog$_{2}$n)")
                plt.pause(0.01)
                plt.clf()
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = key
    numBuckets = 5
    maxElement = max(l)
    minElement = min(l)
    rnge = (maxElement - minElement) / numBuckets
    temp = []
    for i in range(numBuckets):
        # print(i)
        temp.append([])
    for i in range(len(l)):
        diff = (l[i] - minElement) / rnge - int((l[i] - minElement) / rnge)
        if (diff == 0 and l[i] != minElement):
            temp[int((l[i] - minElement) / rnge) - 1].append(l[i])
        else:
            temp[int((l[i] - minElement) / rnge)].append(l[i])
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            insertion(temp[i])
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                l[k] = i
                k = k + 1


# def radixSort(l):
#     def helperCountingSort(arr, exp):
#         n = len(arr)
#         output = [0] * n
#         count = [0] * 10
#         for i in range(0, n):
#             index = arr[i] // exp
#             count[index % 10] += 1
#         for i in range(1, 10):
#             count[i] += count[i - 1]
#         i = n - 1
#         while i >= 0:
#             index = arr[i] // exp
#             output[count[index % 10] - 1] = arr[i]
#             count[index % 10] -= 1
#             i -= 1
#         i = 0
#         for i in range(0, n):
#             arr[i] = output[i]
#
#     max1 = max(l)
#     exponent = 1
#     while max1 / exponent >= 1:
#         helperCountingSort(l, exponent)
#         exponent *= 10


# def countingSort(l):
#     n = len(l)
#     maxElement = max(l)
#     minElement = min(l)
#     rnge = maxElement - minElement + 1
#     countList = [0 for _ in range(rnge)]
#     outputList = [0 for _ in range(n)]
#     for i in range(0, n):
#         countList[l[i] - minElement] += 1
#     for i in range(1, len(countList)):
#         countList[i] += countList[i - 1]
#     for i in range(n - 1, -1, -1):
#         outputList[countList[l[i] - minElement] - 1] = l[i]
#         countList[l[i] - minElement] -= 1
#     for i in range(0, n):
#         l[i] = outputList[i]

bubbleSort(bubbleList)
plt.bar(bubblex, bubbleList)
plt.title("Bubble Sort O(n$^{2}$)")
plt.show()
selectionSort(selectionList)
plt.bar(selectionx, selectionList)
plt.title("Selection Sort O(n$^{2}$)")
plt.show()
insertionSort(insertionList)
plt.bar(insertionx, insertionList)
plt.title("Insertion Sort O(n$^{2}$)")
plt.show()
heapSort(heapList)
plt.bar(heapx, heapList)
plt.title("Heap Sort O(nlog$_{2}$n)")
plt.show()
quickSort(quickList)
plt.bar(quickx, quickList)
plt.title("Quick Sort O(nlog$_{2}$n)")
plt.show()
shellSort(shellList)
plt.bar(shellx, shellList)
plt.title("Shell Sort O(n$^{2}$)")
plt.show()
bucketSort(bucketList)
plt.bar(bucketx, bucketList)
plt.title("Bucket Sort O(nlog$_{2}$n)")
plt.show()
