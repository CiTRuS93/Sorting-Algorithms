# Python program for implementation of MergeSort
# Merges two subarrays of arr[].
# First subarray is arr[l..middle]
# Second subarray is arr[middle+1..right]


def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[middle + 1 + j]

    # Merge the temp arrays back into arr[left..right]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, left, right):
    if left < right:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (left+(right-1))//2

        # Sort first and second halves
        mergeSort(arr, left, m)
        mergeSort(arr, m+1, right)
        merge(arr, left, m, right)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
print(arr)

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
print(arr)
