import random
import time

# IMPLEMENTATION OF BINARY SEARCH ALGORITHM

# we will prove that binary search is more efficient than naive search

# Naive Search: scan entire list and ask if its equal to the target,

# if yes, return the index,
# if not, then return -1

def naive_search(l, target):
    # example = [1,2,3,4,5,6,7,8,9]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary Search: uses a SORTED list, and then compares values against each other to find the answer
# without having to iterate through the entire list
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1


    # example = [1,3,6,9,10,11,17,18,29] # if our target is 11 it should return index 5
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target < l[midpoint]:
        return binary_search(l, target, midpoint+1, high)


if __name__=="__main__":
    l = [1,3,6,9,10,11,17,18,29]
    target = 18
    print(naive_search(l, target))
    print(binary_search(l, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    start =  time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end-start)/length, "seconds")

    start =  time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end-start)/length, "seconds")
