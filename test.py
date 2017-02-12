# CS350 Project
# Jiaqi Luo
# 3/6/2016
import random
import time 
from selectionSort import selectionsort
from insertionSort import insertionsort
from mergeSort     import mergesort
from bucketSort    import bucketsort
from quickSort     import quicksort
from heapSort      import heapsort



#-----------------------------------------------------
#         Data Crafter
#-----------------------------------------------------
def randomArray(arraySize, dataRange):
    array = []
    for i in range(arraySize):
	array.append(random.randrange(0, dataRange))
    return array


def increasingArray():
    array = randomArray(100000,1000000)
    quicksort(array)
    return array


def reversedArray():
    array = randomArray(100000,1000000)
    insertionsort(array)
    array.reverse()
    return array

def oneValueArray(arraySize, value):
    array = []
    for i in range(arraySize):
	array.append(value)
    return array




if __name__ == "__main__":
    array = randomArray(100000,1000000)
    nearlySorted = increasingArray() 
    reverse = reversedArray()


#===================================================================
    temp = list(nearlySorted)
    start = time.time()
    #-------------------------
    selectionsort(temp)
    #-------------------------
    end = time.time()
    elapsed = end - start
    print "Selection sort:  ", elapsed
#===================================================================
#===================================================================
    temp = list(nearlySorted)
    start = time.time()
    #-------------------------
    insertionsort(temp)
    #-------------------------
    end = time.time()
    elapsed = end - start
    print "inseretion sort:  ", elapsed
#===================================================================
#===================================================================
    temp = list(nearlySorted)
    start = time.time()
    #-------------------------
    mergesort(temp)
    #-------------------------
    end = time.time()
    elapsed = end - start
    print "merge sort:  ", elapsed
#===================================================================
#===================================================================
    temp = list(nearlySorted)
    start = time.time()
    #-------------------------
    bucketsort(temp)
    #-------------------------
    end = time.time()
    elapsed = end - start
    print "bucket sort:  ", elapsed
#===================================================================
#===================================================================
    temp = list(nearlySorted)
    start = time.time()
    #-------------------------
    quicksort(temp)
    #-------------------------
    end = time.time()
    elapsed = end - start
    print "quick sort:  ", elapsed
#===================================================================
#===================================================================
    temp = list(nearlySorted)
    start = time.time()
    #-------------------------
    heapsort(temp)
    #-------------------------
    end = time.time()
    elapsed = end - start
    print "heap sort:  ", elapsed
#===================================================================
#===================================================================
    temp = list(nearlySorted)
    start = time.time()
    #-------------------------
    sorted(temp)
    #-------------------------
    end = time.time()
    elapsed = end - start
    print "built in  sort:  ", elapsed
#===================================================================

