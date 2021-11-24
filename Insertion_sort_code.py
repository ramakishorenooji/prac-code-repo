# Insertion sort code
def insertion_sort(arr):
    # insertion sort algorithm
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [5, 3, 1, 6, 2, 9, 100, 111]
insertion_sort(arr)
for i in range(len(arr)):
    print(f"{arr[i]}", end=" ")
