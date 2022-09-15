from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        print(n)
        raise ValueError()
    return digits

def initializeB(A, v):
    B=list()
    for i in range(len(A)):
        B.append((A[i][0], (A[i][1], v[i])))
    return B

def RadixSort(U,b,A):
    k= int(math.log(U,b))
    vPrimes=list()
    for i in range(len(A)):
        vPrime=BC(A[i][0],b,k)
        vPrimes.append(vPrime)
    B=initializeB(A, vPrimes)
    for j in range(k):
        for i in range(len(A)):
            kPrime=B[i][1][1][j]
            B[i]= (kPrime,(B[i][1][0],B[i][1][1]))
        B=countSort(b, B)
    for i in range(len(A)):
        A[i][0]=0
        for j in range(len(vPrimes[i])):
            A[i][0] += B[i][1][1][j]*(b**j)
        A[i][1]=B[i][1][0]
    return A

# print(RadixSort(10,10,[[9,'apple'],[8,'banana']]))


def test(n,U):
    Count=0
    Merge=0
    Radix=0
    for i in range(5):
        lst=list()
        for j in range(n):
            lst.append([random.randint(0,U-1),j])
        lstMerge=lst
        lstRadix=lst
        lstCount=lst

        start=time.time()
        countSort(U, lstCount)
        end=time.time()
        Count+=(end-start)

        start=time.time()
        mergeSort(lstMerge)
        end=time.time()
        Merge+=(end-start)

        start=time.time()
        RadixSort(U, 2, lstRadix)
        end=time.time()
        Radix+=(end-start)
    print(Count/5)
    print(Merge/5)
    print(Radix/5)
    
    if Merge<Radix: print("merge passed rad")
    if Radix<Count: print("rad passed count")

test(2**16,2**7)

# k= int(math.log(4,4))