def binary_search (list, item):
    # low and high keep track of which part of the list you'll search in
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low+high)//2
        guess=list[mid] # check the middle element
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list=[1, 3, 5, 7, 9]

print (binary_search(my_list, 3))

print (binary_search(my_list, -1))
