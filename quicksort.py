# -*- coding: utf-8 -*-

def quicksort(A,l,h) :
    if (l < h) :
        pivot_location = partition(A,l,h)
        quicksort(A,l,pivot_location)
        quicksort(A,pivot_location+1,h)
        
def partition(A,l,h) :
    pivot = A[l]
    leftwall = l
    
    t = 0
    for i in range(l+1,h) :
        if (A[i]<pivot) :
            t = A[i]
            A[i] = A[leftwall]
            A[leftwall] = t
            leftwall += 1
            
    t = pivot 
    pivot = A[leftwall]
    A[leftwall] = t
    
    return (leftwall)