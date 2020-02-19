def bubblesort(arr):
    n=len(arr)-1 #6

    for i in range(n-1): #5
        for j in range(n): #6 
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
   # return arr

arr = [64, 34, 25, 12, 22, 11, 90]

bubblesort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])
