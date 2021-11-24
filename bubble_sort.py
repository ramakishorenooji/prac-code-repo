arr = [500,45,1,3,5,3]

def bubble_sort(arr):
    n = len(arr) #get array length
    for i in range(n-1): #Need compare elements with each other, need 2 for loop for it
        for j in range(0,n-i-1): #second loop is obtained by reducing the first lenght
            
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j+1],arr[j]
    
    return(arr)   

result = bubble_sort(arr)
print(result)