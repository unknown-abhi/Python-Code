import sys
#Bubble Sort.
def bubbleSort(arr, n):
    for i in range(n-1):  
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Selection Sort.
def selectionSort(arr, n):
    for i in range(n):
        min_idx = i 
        for j in range(i+1, n): 
            if (arr[min_idx] > arr[j]): 
                min_idx = j          
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#Insertion Sort.
def insertionSort(arr, n):  
    for i in range(1, n): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

print("Basic Sorting Techniques as a Menu Driven Program.")

n = int(input("\nEnter no. of elements u want to sort : "))
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

print("\nPlease select any option Given Below for Sorting : ")

while(1):
    print("\n1. Bubble Sort.\n2. Selection Sort.\n3. Insertion Sort.\n4. Exit")
    ch = int(input("\nEnter your Choice : "))
    if(ch==1):
        bubbleSort(arr, n)
        print ("Sorted array is:")
        print(*arr, sep = ", ")
    elif(ch==2):
        selectionSort(arr, n)
        print ("Sorted array is:")
        print(*arr, sep = ", ")
    elif(ch==3):
        insertionSort(arr, n)
        print ("Sorted array is:")
        print(*arr, sep = ", ")
    elif(ch==4):
        break
    else:
        print("\nPlease Select only 1-4 option.\n")
