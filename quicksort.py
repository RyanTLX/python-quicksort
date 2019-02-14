# In place quicksort implementation with random pivot using Lomuto partition scheme.
# Tan Ryan

from random import randint


# Lomuto partition scheme
# Set pointer i to low-1 as starting point
# Iterate array from index low to high with pointer j
#   If element at j is lower than pivot (array[high] according to Lomuto partition scheme)
#     Increment pointer i
#     Swap elements of pointer i and j
# When partioning is complete, pivot should belong to new index at i+1
# So swap elements of old and new pivot indexes
# Return new pivot index for next round of recursion at quicksort()
def partition(array, low, high):
  pivotValue = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivotValue:
      i += 1
      array[i], array[j] = array[j], array[i]
  
  newPivotIndex = i + 1
  array[newPivotIndex], array[high] = array[high], array[newPivotIndex]
  return newPivotIndex


# Pick random element as pivot
# Swap random element with last element (Lomuto partition scheme)
# Call partition() to perform Lomuto partition
# Return new pivot index from partition() for next round of recursion at quicksort()
def partition_r(array, low, high):
  randomIndex = randint(low, high)
  array[randomIndex], array[high] = array[high], array[randomIndex]
  return partition(array, low, high)


# Array/sub-array to be sorted, low index, high index
# Returns if low index is same or higher than high index (e.g. empty array)
# Starts partioning by calling partition_r, receiving index of sorted pivot
# Recur quicksort with low partition (elements lower than pivot)
# Recur quicksort with high partition (elements higher than pivot)
def quicksort(array, low, high):
  if low >= high: return
  pivotIndex = partition_r(array, low, high)
  quicksort(array, low, pivotIndex - 1)
  quicksort(array, pivotIndex + 1, high)


if __name__ == "__main__":
    # Create size 10 array of random int from 1-999
    array = []
    for i in range(1, 11):
      array.append(randint(1, 999))

    print("Unsorted:", array)

    # Start in-place quicksort lomuto style.
    quicksort(array, 0, len(array) - 1)
    
    print("  Sorted:", array)