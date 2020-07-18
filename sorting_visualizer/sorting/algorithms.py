
import sys

#Helper method to swap values
def swap(A, x, y):
    A[x], A[y] = A[y], A[x]




#Merge Sort algorithm (A (array), p (starting index), r(final index))
def merge_sort(A, p, r, color_array):
    final = False
    if p<r:
        q = (p+r)//2
        yield from merge_sort(A, p, q, color_array)
        yield from merge_sort(A, q+1, r, color_array)
        if p == 0 and r == len(A)-1:
            final = True
        yield from merge(A, p, q, r, color_array, final)
        yield A

#Merge sort helper
def merge(A, p, q, r, color_array, final):
    new = []
    i = p
    j = q+1
    while(i<=q and j<=r):
        if(A[i]<A[j]):
            new.append(A[i])
            i+=1
        else:
            new.append(A[j])
            j+=1
    if(i>q):
        while(j<=r):
            new.append(A[j])
            j+=1
    else:
        while(i<=q):
            new.append(A[i])
            i+=1
    for i,val in enumerate(new):
        A[p+i] = val
        color_array[p+i] = 1
        yield A
        if not final:
            color_array[p+i] = 0




#Bubble sort algorithm
def bubble_sort(A, color_array):
    didSwap = True
    while didSwap:
        didSwap = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                color_array[i] = 1
                color_array[i+1] = 1
                swap(A,i,i+1)
                yield A
                color_array[i] = 0
                color_array[i+1] = 0
                didSwap = True
    yield A
    for i in range(len(A)):
        color_array[i] = 1
        yield A



#Insertion sort algorithm
def insertion_sort(A, color_array):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            color_array[i+1] = 1
            color_array[i] = 1
            yield A
            color_array[i+1] = 0
            color_array[i] = 0
            i = i-1
        A[i+1] = key
    yield A
    for i in range(len(A)):
        color_array[i] = 1
        yield A


#Quick sort algorithm
def quick_sort(A, p, r, color_array):
    if p<r:
        x = A[p]
        i = p
        for j in range(p+1, r+1):
            if A[j] <= x:
                i+=1
                color_array[j] = 1
                color_array[i] = 1
                yield A
                swap(A,j,i)
                yield A
                color_array[j] = 0
                color_array[i] = 0
                yield A
        color_array[p] = 1
        color_array[i] = 1
        yield A
        swap(A,p,i)
        yield A
        color_array[p] = 0
        color_array[i] = 0
        yield A
        yield from quick_sort(A, p, i-1, color_array)
        yield from quick_sort(A, i+1, r, color_array)
    










# color_array = []
# array = [9,8,7,6,5,4,3,2,1]
# quick_sort(array, 0 , len(array)-1, color_array)
# print(array)