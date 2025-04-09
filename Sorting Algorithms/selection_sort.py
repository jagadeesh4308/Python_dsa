# selects the minimum element in the remaining element and the minimum element will get the starting indexes
# uses swap technique to swap minimum and the current index value

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

print(selection_sort([5,21,6,9,3,1]))