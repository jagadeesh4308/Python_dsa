# selection sort algorithm
# finds the minimum element in the unsorted list and swaps it with the first element
# this process is repeated until the list is sorted
# the time complexity is O(n^2)
# the space complexity is O(1)
def selection_sort(list):
    length = len(list)
    for i in range(length-1):
        minIdx = i
        # search for the minimun index in the remaining list
        for j in range(i+1, length):
            if (list[j] < list[minIdx]): 
                minIdx = j
        # swap the elements
        list[i], list[minIdx] = list[minIdx], list[i]
    return list

# Bubble sort algorithm
#bubbles up the largest element to the end of the list
# uses swap technique to swap the current index value and the next index value
# this process is repeated until the list is sorted
# the time complexity is O(n^2)
# the space complexity is O(1)
def bubble_sort(list):
    length = len(list)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if (list[j] > list[j+1]):
                # swap the elements
                list[j], list[j+1] = list[j+1], list[j]
    return list

def main():
    print('selection:', selection_sort([5,21,6,9,3,1]))
    print('bubble:', bubble_sort([5,21,6,9,3,1]))

main()