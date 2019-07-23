# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # iterates through the array starting at the "Index of [0], for the entire length of the array -1 (goes to the end)"

        # TO-DO: find next smallest element
        smallest_index = i  # create a copy of the entire index

        for j in range(i+1, len(arr)):
            # iterates through the array starting at the second index (i+1 and continues until the end.)
            if arr[smallest_index] > arr[j]:
                # if the array with the current smallest index is less than the new copy of the array
                smallest_index = j
                # make smallest_index become the new array j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # array i and array smallest is assigned array smallest and array i thus swapping them to make the smaller numbers go to the begginging

    return arr


print(selection_sort([11, 33, 22, 55, 44, 77, 66]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    x = len(arr)  # X is the entire length of the array

    for i in range(x):  # iterate over the whole array
        for j in range(0, x-i-1):  # copy array iterating from start to fininsh
            if arr[j] > arr[j+1]:  # if the iteration is smaller than the next iteration
                arr[j], arr[j+1] = arr[j+1], arr[j]  # smaller to the beginning

    return arr


print(bubble_sort([11, 33, 22, 55, 44, 77, 66]))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
