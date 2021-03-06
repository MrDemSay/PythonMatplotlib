#----------------SORT----------------------------
array = [3, 5, 2, 1, 8, 9, 4, 0]

def bubble_sort(array):
    flag = True
    while flag:
        flag = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True
    print(array)

#bubble_sort(array)

def selection_sort(array):
    for i in range(len(array)):
        low_value_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[low_value_index]:
                low_value_index = j
        array[i], array[low_value_index] = array[low_value_index], array[i]
    print(array)

#selection_sort(array)

def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1

        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item_to_insert
    print(array)

#insertion_sort(array)






#--------------------SEARCH----------------------------
def linear_search(array, elem):
    for i in range(len(array)):
        if array[i] == elem:
            print(i)
    return -1

#linear_search(array, 2)



# def binary_search(array, elem):
#     first = 0
#     last = len(array) - 1
#     index = -1
#     while(first <= last) and (index == -1):
#         mid = (first + last) // 2
#         if array[mid] == elem:
#             index = mid
#         else:
#             if elem < array[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     print(index)
# binary_search(array, 2)
