# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # using binary_search after setting the base case to search through the list.
    # needs a start and end point
    # to have a middle so set the middle.

    # Your code here
    # seting base
    # start = 0
    # end = len(arr) - 1
    # start = 0
    # end = len(arr)

    while start <= end:
        mid = (
            end + start
        ) // 2  # this finds the mid point between the high end and low end.
        if arr[mid] < target:

            return binary_search(arr, target, mid + 1, end)
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        else:
            return mid
    else:

        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


# failed things:
# if end is None:
#         end = len(arr) - 1
#     if start > end:
#         return False
#     # element is the middle so just return it
#     mid = (start + end) // 2
#     if target == arr[mid]:
#         return mid
#     # if its smaller then only check left side of array
#     elif target < arr[mid]:
#         return binary_search(arr, target, start, mid - 1)
#     # flip it reverse it from waht i did up there^
#     else:
#         return binary_search(arr, target, mid + 1, end)
#     # return nothin' if the number doesn't exist
#     # else:
#     #     print("ahh, shoot it never made it into the if")
#     #     return -1
